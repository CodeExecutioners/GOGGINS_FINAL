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



	
class LessonsPage(BaseHandler):

	def get(self):
		
		user = self.session.get('user')
		logging.debug(user)
		#models.Users.insertUser('fisherr', 'goggins', 'fisher.robert26@gmail.com')
		
		#get all cities
		#models.LessonType.insert('Private')
		#models.LessonType.insert('Group')
		#models.LessonType.insert('Drop-In')
		#models.LessonCity.insertCity('City1')
		
		cities = models.LessonCity.getAllCities()
		logging.debug(cities.get())
		types = models.LessonType.getAllTypes()
		#testType = types.get()
		#testType.cities.append(cities.get().key)
		
		#testCity = cities.get()
		#testCity.lessons.append(allLessons.get().key)
		
		#models.LessonCompositeKeys.insertLesson(type_key, city_key, 'date', 'time', 'location', 'cost', 'details')
		allLessons = models.LessonCompositeKeys.getAllLessons()
		logging.debug(allLessons.get())
		
		
		cities = models.LessonCity.getAllCities()
		template_values ={'user': user, 'types': types, 'lessons': allLessons, 'cities': cities}
		template = JINJA_ENVIRONMENT.get_template('templates/lessons.html')
		self.response.write(template.render(template_values))
		
		#insert a type with repeated properties
		
		
		
		
	
	def post(self):
		logging.debug("LessonsPage Post start")
		#get all the table data
		jsonstring = self.request.body
		self.response.out.write(jsonstring)
		jsonObject = json.loads(jsonstring)
		#typeIndex = 1
		id = jsonObject[0]['value']
		type = jsonObject[1]['value']
		city = jsonObject[2]['value']
		location = jsonObject[3]['value']
		date = jsonObject[4]['value']
		time = jsonObject[5]['value']
		cost = jsonObject[6]['value']
		details = jsonObject[7]['value']
		link = jsonObject[8]['value']
		
		#Type = LessonType.get_by_id(int(typeid))
		models.LessonCompositeKeys.updateLessonByID(id, type, city, date, time, location, cost, details, link)
		#models.LessonTest.insertLesson(type, city, date, time, location, cost, details)
		logging.debug("LessonsPage Post done")
		#self.redirect('/lessons')	

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}			

app = webapp2.WSGIApplication([
			('/lessons', LessonsPage),
			],config = config,
			debug=True)