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
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



	
class LessonsPage(BaseHandler):

	def get(self):
		user = self.session.get('user')
		logging.debug(user)
		types = models.LessonType.getAllTypes()
		
		
		#get typeKeys
		private_key = models.LessonType.getLessonTypeByName('Private & Group Lessons (by appointment)').key
		drop_key = models.LessonType.getLessonTypeByName('Group Lessons/Dances Drop-In').key
		logging.debug(drop_key)
		group_key = models.LessonType.getLessonTypeByName('Group Lessons (4-6 week sessions)').key
		logging.debug(group_key)
		privateLessons = models.LessonComposite.getAllLessonsByType(private_key)
		dropInlessons = models.LessonComposite.getAllLessonsByType(drop_key)
		groupLessons = models.LessonComposite.getAllLessonsByType(group_key)
		template_values ={'user': user, 'types': types, 'privateLessons': privateLessons,'dropInLessons':dropInlessons, 'groupLessons': groupLessons}
		template = JINJA_ENVIRONMENT.get_template('templates/lessons.html')
		self.response.write(template.render(template_values))
		
	
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
		
		#Type = LessonType.get_by_id(int(typeid))
		models.LessonTest.updateLessonByID(id, type, city, date, time, location, cost, details)
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