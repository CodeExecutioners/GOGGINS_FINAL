import os
import urllib
import webapp2
import jinja2
import models
import logging
import json
from main import BaseHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class ResourcesPage(BaseHandler):
	def get(self):

		resources = models.Resource.getAllResources()
		users = self.session.get('user')
		template_values ={'user':users, 'resources': resources}
		template = JINJA_ENVIRONMENT.get_template('templates/resources.html')
		self.response.write(template.render(template_values))

	def post(self):

		jsonstring = self.request.body
		logging.debug(jsonstring)
		self.response.out.write(jsonstring)
		jsonResources = json.loads(jsonstring)
		logging.debug(jsonResources)
		for resource in jsonResources:
			id = resource['ID']
			desc = resource['DATA']
			models.Resource.updateResourceDescByID(id, desc)
		logging.debug('post end')
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/resources', ResourcesPage)],
                              config=config, debug=True)