import os
import urllib
import urllib2
import webapp2
import jinja2
import models
import json
from main import BaseHandler
from google.appengine.ext import ndb
from datetime import datetime
import sys
import logging
from webapp2_extras import sessions

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape',"jinja2.ext.do"],
    autoescape=True)


	
class DancesPage(BaseHandler):

	def get(self):
		resources = models.Resource.getAllResources()
		users = self.session.get('user')
		template_values ={'user':users, 'resources': resources}
		template = JINJA_ENVIRONMENT.get_template('templates/dances.html')
		self.response.write(template.render(template_values))
		
		

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}			

app = webapp2.WSGIApplication([
			('/dances', DancesPage),
			],config = config,
			debug=True)