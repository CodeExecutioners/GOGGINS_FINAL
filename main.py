#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import webapp2
import jinja2
import models
import logging
from webapp2_extras import sessions
from google.appengine.api import users
from google.appengine.api import mail
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def handle_404(request, response, exception):
    logging.exception(exception)
    template_values = {}
    response.set_status(404)
    template = JINJA_ENVIRONMENT.get_template('templates/default_error.html')
    response.write(template.render(template_values))

def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    template_values = {}
    template = JINJA_ENVIRONMENT.get_template('templates/default_error.html')
    response.write(template.render(template_values))

class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        # Log the error.
        logging.exception(exception)

        # Set a custom message.
       

        # If the exception is a HTTPException, use its error code.
        # Otherwise use a generic 500 error code.
        if isinstance(exception, webapp2.HTTPException):
            self.response.set_status(exception.code)
        else:
            self.response.set_status(500)

    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
 
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
 
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

		
		

class LogoutHandler(BaseHandler):
	def get(self):
		if self.session.get('user'):
			del self.session['user']
		self.redirect('/')


class LoginHandler(BaseHandler):
	def get(self):
		
		if self.session.get('user'):
			del self.session['user']
		if not self.session.get('referrer'):
			self.session['referrer'] = \
				self.request.environ['HTTP_REFERER'] \
				if 'HTTP_REFERER' in self.request.environ \
				else '/'
		template_values = {
		}
		template = JINJA_ENVIRONMENT.get_template('templates/login.html')
		self.response.write(template.render(template_values))
	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')
		loginSuccess = models.Users.loginProcess(username, password)
		
		
		if(loginSuccess):
			self.session['user'] = username
			self.redirect('/')
			#self.redirect('/adminLessons')
		else:
			self.redirect('/login')

class RecoverHandler(BaseHandler):
	def get(self):
		template_values = {}
		template = JINJA_ENVIRONMENT.get_template('templates/recover.html')
		self.response.write(template.render(template_values))

	def post(self):
		username = self.request.get('username')
		password = models.Users.getPassword(username)
		email = models.Users.getEmail(username)
		logging.debug('The password: ' + password)
		logging.debug('Email:' + email)
		gogginsBody = ("""
Dear """+username+""",

This is your recovered password:

"""+password+"""


From,

DancinGoggin.com
""")
		logging.debug("Sending Password Recovery Email")
		mail.send_mail("fisher.robert26@gmail.com",email,"Password Recovery", gogginsBody)
		logging.debug("sent Goggin's Password Recovery email")
		self.redirect('/')

class ChangeHandler(BaseHandler):
	def get(self):
		template_values = {}
		template = JINJA_ENVIRONMENT.get_template('templates/change.html')
		self.response.write(template.render(template_values))

	def post(self):
		username = self.request.get('username')
		oldPass= self.request.get('password')
		newPass = self.request.get('newPass')
		if(models.Users.resetPassword(username,oldPass,newPass)=="True"):
			self.redirect('/')
		else:
			#self.response.write("Invalid password")
			self.redirect('/change')
		
			
class MainHandler(BaseHandler):
	def get(self):
		user = self.session.get('user')
		logging.debug(user)
		resources = models.Resource.getAllResources()
		template_values = {'user': user, 'resources': resources}
		path = self.request.path
		template = JINJA_ENVIRONMENT.get_template('templates/index.html')
		self.response.write(template.render(template_values))

class SubmitForm(webapp2.RequestHandler):
	def post(self):
		firstname = self.request.get('firstname')
		lastname = self.request.get('lastname')
		email = self.request.get('email')
		phone = self.request.get('phone')
		message = self.request.get('message')
		emailItem = models.Email(firstname = firstname,lastname = lastname,	email = email,phone = phone,message = message)
		emailItem.put()
		self.redirect('/')
		
config = {}
config['webapp2_extras.sessions'] = {
	'secret_key': 'my-super-secret-key',
}	


		
app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	('/submit', SubmitForm),
	('/recover',RecoverHandler),
	('/change',ChangeHandler),

], config=config,debug=True)
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500