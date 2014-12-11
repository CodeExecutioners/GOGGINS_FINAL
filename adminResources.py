import os
import urllib
import urllib2
import webapp2
import logging
import jinja2
import models
import json
from google.appengine.ext import ndb
from datetime import datetime
import sys
import time

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class AdminResourcesPage(webapp2.RequestHandler):
	def get(self):
		logging.debug('post')
		#models.Resource.deleteAllResources()

		#get all resources
		resources = models.Resource.getAllResources()
		
        #self.response.write('Hello world!')
		template_values ={'resources':resources}
		template = JINJA_ENVIRONMENT.get_template('templates/adminResources.html')
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
	

app = webapp2.WSGIApplication([('/adminResources', AdminResourcesPage)],
                              debug=True)