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

		if 'Delete' in self.request.POST:
			id = self.request.get("resID")
			models.Resource.deleteResourceByID(id)
		else:
			type = self.request.get("resType")
			title = self.request.get("resTitle")
			linkOrAddress = self.request.get("resAddress")
			desc = self.request.get("resDesc")
			id = self.request.get("resID")
			
			if id == "000":
				id = 'None'
			
			models.Resource.updateResourceByID(id, type, title, linkOrAddress, desc)
			
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/resources', ResourcesPage)],
                              config=config, debug=True)