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

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class AdminResourcesPage(webapp2.RequestHandler):
	def get(self):
		#models.Resource.deleteAllResources()

		#get all resources
		resources = models.Resource.getAllResources()
		
        #self.response.write('Hello world!')
		template_values ={'resources':resources}
		template = JINJA_ENVIRONMENT.get_template('templates/adminResources.html')
		self.response.write(template.render(template_values))
		
	def post(self):
		jsonstring = self.request.body
		self.response.out.write(jsonstring)
		jsonObject = json.loads(jsonstring)
		
		models.Resource.deleteAllResources()
		
		#update or insert
		for resource in jsonObject:
			type = resource['Type']
			title = resource['Title']
			linkOrAddress = resource['Link or Address']
			desc = resource['Desc']
			models.Resource.updateResourceByID(type, title, linkOrAddress, desc)
			#models.Lesson.insertLesson(id, city, date, location, cost)
			
		#for location in jsonObject:
		#	title = location['Title']
		#	link = location['Link']
		#	desc = location['Desc']
		#	address = location['Address']
		#	models.Location.updateLocationByID(title, link, desc, address);
			#models.Lesson.insertLesson(id, city, date, location, cost)
		
	

app = webapp2.WSGIApplication([('/adminResources', AdminResourcesPage)],
                              debug=True)