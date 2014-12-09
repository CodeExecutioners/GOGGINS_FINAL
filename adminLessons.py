import os
import urllib
import urllib2
import webapp2
import jinja2
import models
import json
from google.appengine.ext import ndb
from datetime import datetime
from main import BaseHandler
import sys
import logging
import webapp2

from webapp2_extras import sessions
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AddLesson(BaseHandler):
	def get(self):
		logging.debug("Add Lesson GET START")
		types = models.LessonType.getAllTypes()
		template_values ={'types': types}
		template = JINJA_ENVIRONMENT.get_template('templates/addLesson.html')
		self.response.write(template.render(template_values))
		logging.debug("AddLesson Get done")
		
	
	
class UpdateLesson(BaseHandler):
	def post(self):
		logging.debug("Update Lesson Post start")
		#get all the table data
		jsonstring = self.request.body
		self.response.out.write(jsonstring)
		jsonObject = json.loads(jsonstring)
		
		#get the values
		id = jsonObject[0]['value']
		type_name = jsonObject[1]['value']
		city_name = jsonObject[2]['value']
		location = jsonObject[3]['value']
		date = jsonObject[4]['value']
		time = jsonObject[5]['value']
		cost = jsonObject[6]['value']
		details = jsonObject[7]['value']
		link = jsonObject[8]['value']
		
		
		#insert city if new
		city = models.LessonCity.getLessonCityByName(city_name)
		if city == None:
			logging.debug("CITY NOT FOUND, adding new city")
			city = models.LessonCity.insertCity(city_name)
		else:
			logging.debug("CITY FOUND!")
		logging.debug(city)
		
		type = models.LessonType.getLessonTypeByName(type_name)
		
		if type == None:
			logging.debug("TYPE NOT FOUND, adding new type")
			type = models.LessonType.insert(type_name)
		logging.debug(type)
		
		
		

		#update or insert
		models.LessonCompositeKeys.updateLessonByID(id, type.key, city.key, date, time, location, cost, details, link)
		
		logging.debug("UPDATE LESSON POST DONE")
			
		
	
	
class EditLesson(BaseHandler):
	def post(self):
		logging.debug("EditLesson POST start")
		id = self.request.body
		logging.debug("id: " +id)
		types = models.LessonType.getAllTypes()
		cities = models.LessonCity.getAllCities()
		lesson = models.LessonCompositeKeys.getLessonByID(id)
		template_values ={'lesson':lesson, 'types': types, 'cities': cities}
		template = JINJA_ENVIRONMENT.get_template('templates/editLesson.html')
		self.response.write(template.render(template_values))
		logging.debug("EditLesson Get done")
	
class DeleteLesson(BaseHandler):
	def post(self):
		logging.debug("DELETE LessonTest POST start")
		id = self.request.body
		logging.debug("id: " +id)
		lesson = models.LessonCompositeKeys.deleteLessonByID(id)
		
		self.response.write("deleted")
		logging.debug("DeleteLesson Get done")
		
	
class DeleteType(BaseHandler):
	def post(self):
		logging.debug("DELETE LessonTYPE POST start")
		id = self.request.body
		logging.debug("id: " +id)
		type = models.LessonType.deleteLessonTypeByID(id)
		
		#delete all lessson in type
		logging.debug(type)
		models.LessonCompositeKeys.deleteAllLessonsByType(type.key)
		logging.debug("DeleteLesson Get done")
		
class DeleteCity(BaseHandler):
	def post(self):
		logging.debug("DELETE LessonCity POST start")
		id = self.request.body
		logging.debug("id: " +id)
		type = models.LessonCity.deleteLessonCityByID(id)
		self.response.write("deleted type")
		logging.debug("DeleteLesson Get done")
		
	

	
class AdminLessonsPage(BaseHandler):
	def get(self):
		#models.LessonTest.deleteAllLessons()
		user = self.session.get('user')
		logging.debug(user)
		if user == None:
			self.redirect('/login')
		privateLessons = models.LessonTest.getAllLessonsByType('Private & Group Lessons (by appointment)')
		dropInlessons = models.LessonTest.getAllLessonsByType('Group Lessons/Dances Drop-In')
		groupLessons = models.LessonTest.getAllLessonsByType('Group Lessons (4-6 week sessions)')
		
		#get LessonTest by city
		template_values ={'privateLessons': privateLessons,'dropInLessons':dropInlessons, 'groupLessons': groupLessons}
		template = JINJA_ENVIRONMENT.get_template('templates/adminLessons.html')
		self.response.write(template.render(template_values))
		
	

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}		
app = webapp2.WSGIApplication([
		('/adminLessons', AdminLessonsPage),
		('/addLesson', AddLesson),
		('/updateLesson', UpdateLesson),
		('/editLesson', EditLesson),
		('/deleteLesson', DeleteLesson),
		('/deleteType', DeleteType),
		('/deleteCity', DeleteCity)
		],config = config, debug=True)