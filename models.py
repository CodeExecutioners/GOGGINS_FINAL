import webapp2
import datetime
import logging
import math
from google.appengine.ext import ndb
from google.appengine.ext import db





class LessonType(ndb.Model):
	typename = ndb.StringProperty()
	cities = ndb.KeyProperty(repeated=True)
	@classmethod
	def getAllTypes(self):
		try:
			return self.query().order(self.typename)
		except:
			logging.error('getAllTypes failed')
			
	@classmethod
	def getLessonTypeByName(self, typename):
		try:
			logging.debug("getLessonTypeByName start")
			logging.debug("typename: " + typename)
			type= self.query(self.typename == typename)
			if type != None:
				return type.get()
			else:
				return None
		except:
			logging.error('getLessonTypeByName failed')
	
	@classmethod
	def getLessonTypeByID(self, id):
		try:
		
			if(id != 'None'):
				type = LessonType.get_by_id(int(id))
				logging.debug("getLessonTypeByID")
				logging.debug(type)
				return type
				
				
		except:
			logging.error('getLessonTypeByID failed')
		
	@classmethod
	def insert(self, typename):
			logging.debug('insertType start')
			
			try:
				
				type = self(typename = typename, cities = [])
				type.put()
				return type
				logging.debug('insertTypeCities success')
			except:
				logging.error('insertTypeCities failed')
		
	@classmethod
	def deleteLessonTypeByID(self, id):
			try:
			
				if(id != 'None'):
					delete_lesson = LessonType.get_by_id(int(id))
					lesson = delete_lesson
					delete_lesson.key.delete()
					return lesson
					logging.debug('deleteLessonByID success')
					#delete all cities in that type
					
					
			except:
				logging.error('deleteLessonByID failed')
		


		
		
		



class LessonCompositeKeys(ndb.Model):
	"""Models an individual lesson"""
	#should really use date time property
	type_key = ndb.KeyProperty()
	city_key = ndb.KeyProperty()
	date = ndb.StringProperty()
	time = ndb.StringProperty()
	location = ndb.StringProperty()
	cost = ndb.StringProperty()
	details = ndb.TextProperty()
	link = ndb.StringProperty()
	
	@classmethod
	def getAllLessons(self):
		try:
			return self.query()
		except:
			logging.error('getAllLessons failed')
	
	@classmethod
	def getAllLessonsByType(self, type_key):
		#Group, DropIn
		try:
			logging.debug("getAllLessonsByType start")
			return self.query(self.type_key==type_key)
		except:
			logging.error('getAllLessonsByType failed')
	
	
	
	@classmethod
	def getNLessons(self, n):
		try:
			return self.query().fetch(n)
		except:
			logging.error('getNLesssons failed')
	
	#insert
	@classmethod
	def insertLesson(self, type_key, city_key, date, time, location, cost, details, link):
			logging.debug('insertLesson start')
			detailsText = db.Text(details)
			try:
				logging.debug("creating lesson")
				lesson = self(type_key = type_key, city_key = city_key, date = date, time = time, location = location, cost = cost, details = detailsText, link = link)
				lesson.put()
				logging.debug('insertLesson success')
				return lesson
			except:
				logging.error('insertLesson failed')
		
	
	#insert
	@classmethod
	def updateLessonByID(self, id, type_key, city_key, date, time,  location, cost, details, link):
			
			
			try:
				logging.debug("updateLessonByID start")
				if(id != 'None'):
					logging.debug(id)
					updated_lesson = LessonCompositeKeys.get_by_id(int(id))
					
				
					if(updated_lesson != None):
					
						
						updated_lesson.city_key =city_key
						updated_lesson.type_key = type_key
						updated_lesson.date = date
						updated_lesson.time = time
						updated_lesson.location = location
						updated_lesson.cost = cost
						detailsText = db.Text(details)
						updated_lesson.details = detailsText
						updated_lesson.link = link
						updated_lesson.put()
						logging.debug('updateLesson success')
				else:
					logging.debug('Inserting new record')
					self.insertLesson(type_key, city_key, date, time,  location, cost, details, link)
			except:
				logging.error('updateLesson failed')
		

	@classmethod
	def getLessonByID(self, id):
			try:
			
				if(id != 'None'):
					#lesson_key = ndb.Key(self,id)
					lesson = LessonCompositeKeys.get_by_id(int(id))
					logging.debug(lesson)
					
					return lesson
				else:
					logging.debug('Get lesson by id failed')
					
			except:
				logging.error('Get lesson by id failed ')
		

	
	#delete
	@classmethod
	def deleteAllLessons(self):
		try:
			lesson_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(lesson_keys)
			logging.debug('deleteAllLessons success')
		except:
			logging.error('deleteAllLessons failed')
	
	
	#delete
	@classmethod
	def deleteAllLessonsByType(self, type_key):
		try:
			logging.debug(type_key)
			lesson_keys = LessonCompositeKeys.query(type_key == type_key).fetch(keys_only=True)
			if lesson_keys != None:
				ndb.delete_multi(lesson_keys)
			logging.debug('deleteAllLessonsType success')
		except:
			logging.error('deleteAllLessonsTYpe failed')
	
		
	#insert
	@classmethod
	def deleteLessonByID(self, id):
			try:
			
				if(id != 'None'):
					
					delete_lesson = LessonCompositeKeys.get_by_id(int(id))
					logging.debug(delete_lesson)
					
					delete_lesson.key.delete()
					logging.debug('deleteLessonByID success')
			except:
				logging.error('deleteLessonByID failed')
		

		
	#filtering
	@classmethod
	def getLessonsByCity(self, city):
		logging.debug('getLessonsByCity started')
		try:
			return self.query(self.city == city);
		except:
			logging.error('getLessonsByCity failed')
			

			
			
			
			
#OLD LESSON COMPOSITE



class LessonCompositeOld(ndb.Model):
	"""Models an individual lesson"""
	#should really use date time property
	type_key = ndb.KeyProperty()
	city = ndb.StringProperty()
	date = ndb.StringProperty()
	time = ndb.StringProperty()
	location = ndb.StringProperty()
	cost = ndb.StringProperty()
	details = ndb.TextProperty()
	
	@classmethod
	def getAllLessons(self):
		try:
			return self.query()
		except:
			logging.error('getAllLessons failed')
	
	@classmethod
	def getAllLessonsByType(self, type_key):
		#Group, DropIn
		try:
			logging.debug("getAllLessonsByType start")
			return self.query(self.type_key==type_key)
		except:
			logging.error('getAllLessonsByType failed')
	
	
	
	@classmethod
	def getNLessons(self, n):
		try:
			return self.query().fetch(n)
		except:
			logging.error('getNLesssons failed')
	
	#insert
	@classmethod
	def insert(self, type_key, city, date, time, location, cost, details):
			logging.debug('insertLesson start')
			detailsText = db.Text(details)
			try:
				logging.debug("creating lesson")
				logging.debug(type_key)
				logging.debug(city)
				lesson = self(type_key = type_key, city = city, date = date, time = time, location = location, cost = cost, details = detailsText)
				lesson.put()
				logging.debug('insertLesson success')
			except:
				logging.error('insertLesson failed')
		
	
	#insert
	@classmethod
	def updateLessonByID(self, id, type_key, city, date, time,  location, cost, details):
			
			
			try:
				logging.debug("updateLessonByID start")
				if(id != 'None'):
					updated_lesson = LessonCompositeOld.get_by_id(int(id))
					logging.debug(updated_lesson)
				
					if(updated_lesson != None):
					
						logging.debug("Updated city" + updated_lesson.city)
						#updated_lesson.city_key =city_key
						#updated_lesson.city = city_key.cityname
						updated_lesson.city = city
						updated_lesson.type_key = type_key
						updated_lesson.date = date
						updated_lesson.time = time
						updated_lesson.location = location
						updated_lesson.cost = cost
						detailsText = db.Text(details)
						updated_lesson.details = detailsText
						updated_lesson.put()
						logging.debug('updateLesson success')
				else:
					logging.debug('Inserting new record')
					self.insert(type_key, city, date, time,  location, cost, details)
			except:
				logging.error('updateLesson failed')
		

	@classmethod
	def getLessonByID(self, id):
			try:
			
				if(id != 'None'):
					#lesson_key = ndb.Key(self,id)
					lesson = LessonCompositeOld.get_by_id(int(id))
					logging.debug(lesson)
					
					return lesson
				else:
					logging.debug('Get lesson by id failed')
					
			except:
				logging.error('Get lesson by id failed ')
		

	
	#delete
	@classmethod
	def deleteAllLessons(self):
		try:
			lesson_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(lesson_keys)
			logging.debug('deleteAllLessons success')
		except:
			logging.error('deleteAllLessons failed')
		
	#insert
	@classmethod
	def deleteLessonByID(self, id):
			try:
			
				if(id != 'None'):
					delete_lesson = LessonCompositeOld.get_by_id(int(id))
					delete_lesson.key.delete()
					logging.debug('deleteLessonByID success')
			except:
				logging.error('deleteLessonByID failed')
		

		
	#filtering
	@classmethod
	def getLessonsByCity(self, city):
		logging.debug('getLessonsByCity started')
		try:
			return self.query(self.city == city);
		except:
			logging.error('getLessonsByCity failed')
			
		
class LessonCity(ndb.Model):
	cityname = ndb.StringProperty()
	lessons = ndb.KeyProperty(repeated=True)
	@classmethod
	def getAllCities(self):
		try:
			logging.debug("getAllCities started")
			return self.query().order(self.cityname)
		except:
			logging.error('getAllCities failed')
			
	@classmethod
	def getLessonCityByName(self, cityname):
		try:
			logging.debug("searching for city: " +cityname)
			city = self.query(self.cityname == cityname)
			logging.debug(city)
			if city != None:
				
				return city.get()
			else:
				
				return None
		except:
			logging.error('getAllCities failed')
					
	@classmethod
	def insertCity(self, cityname):
		logging.debug('insertCity start')
		try:
			city = self(cityname = cityname)
			city.put()
			return city
			logging.debug('insertCity success')
		except:
			logging.error('insertCity failed')
	@classmethod
	def addLessonToCity(self, lesson_key):
		try:
			logging.debug("addLessonToCity start")
			
			#lesson = LessonCity.getLessonById(lesson_id)
		
			
			#city.lesson_list.append(lesson_key)
			logging.debug('addLessonToCity success')
		except:
			logging.error('addLessonToCity failed')
	@classmethod
	def deleteLessonCityByID(self, id):
			try:
			
				if(id != 'None'):
					delete_lesson = LessonCity.get_by_id(int(id))
					delete_lesson.key.delete()
					logging.debug('deleteLessonByID success')
			except:
				logging.error('deleteLessonCityByID failed')
		
			
	

			
class Email(ndb.Model):
	"""Models an individual email"""
	firstname = ndb.StringProperty()
	lastname = ndb.StringProperty()
	phone = ndb.StringProperty()
	email = ndb.StringProperty()
	message = ndb.StringProperty()

class Users(ndb.Model):
	"""Models an individual user"""
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	email = ndb.StringProperty()
	
	@classmethod
	def getAllUsers(self):
		try:
			return self.query()
		except:
			logging.error('getAllUsers failed')

	#insert
	@classmethod
	def insertUser(self, username, password, email):
		
		try:
			user = self(username=username, password = password, email=email)
			user.put()
			logging.debug('insertUser success')
		except:
			logging.error('insertUser failed')
		
	#delete
	@classmethod
	def deleteAllUsers(self):
		try:
			user_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(user_keys)
		except:
			logging.error('deleteAllUsers failed')
	
		
	#filtering
	@classmethod
	def getUserByUsername(self, username):
		try:
			return self.query(self.username == username);
		except:
			logging.error('getUserByUsername failed')
	
	#return true if user is found, false otherwise
	@classmethod
	def loginProcess(self, username, password):
		loginSuccess = False
		try:
			logging.debug(self.query().count())
			logging.debug(username)
			logging.debug(password)
			loginSuccess = (self.query(self.username == username and self.password==password).count()==1)
			logging.debug('loginProcess success:' + loginSucess)
			return loginSuccess
		except:
			logging.error('loginProcess failed')
			return loginSuccess

	@classmethod
	def getPassword(self, username):
		
		try:
			logging.debug(self.query().count())
			logging.debug(username)
			password=""
			email=""
			password = (self.query(self.username == username).get().password)
			return password
		except:
			logging.error('recover Process failed')

	@classmethod
	def getEmail(self, username):
		try:
			logging.debug("Get Email success")
			logging.debug(self.query().count())
			logging.debug(username)
			password = (self.query(self.username == username).get().email)
			return password
		except:
			logging.error('getEmail Process failed')
	
		
			
	@classmethod
	def resetPassword(self, username,oldPassword,newPassword):
		loginSuccess = False;
		try:
			logging.debug(self.query().count())
			logging.debug(username)
			password = (self.query(self.username == username).get().password)
			logging.debug('The password is:' + password)
			loginSuccess = (self.query(self.username == username and self.password==oldPassword).count()==1)

			if(loginSuccess):
				objeto=(self.query(self.username == username)).get()
				logging.debug("objeto: " + objeto.password)
				objeto.password=newPassword
				objeto.put()
				logging.debug("inserted")
				return "True"
			else:
				logging.debug("Not good")
				return "False"
		except:
			logging.error('recover Process failed')
			return "False"

class Resource(ndb.Model):
	type = ndb.StringProperty()
	title = ndb.StringProperty()
	linkOrAddress = ndb.StringProperty()
	desc = ndb.TextProperty()
	
	@classmethod
	def getAllResources(self):
		try:
			return self.query()
		except:
			logging.error('getAllResource failed')
			
	def getAllResourcesByType(self, type):
		try:
			return self.query(self.type==type)
		except:
			logging.error('getAllLessonsByType failed')
	
	@classmethod
	def getNResources(self, n):
		try:
			return self.query().fetch(n)
		except:
			logging.error('getNResource failed')
	
	#insert
	@classmethod
	def insertResource(self, type, title, linkOrAddress, desc):
		try:
			resource = self(type = type, title = title, linkOrAddress = linkOrAddress, desc = desc)
			resource.put()
			logging.debug('insertResource success')
		except:
			logging.error('insertResource failed')
	

	@classmethod
	def updateResourceByID(self, id, type, title, linkOrAddress, desc):
			logging.debug('updatingResource')
			
			try:
			
				if(id != 'None'):
					updated_resource = Resource.get_by_id(int(id))
					logging.debug(updated_resource)
				
					if(updated_resource != None):
						updated_resource.title =title
						updated_resource.type = type
						updated_resource.linkOrAddress = linkOrAddress
						descText = db.Text(desc)
						updated_resource.desc = descText
						updated_resource.put()
						logging.debug('updateResource success')
				else:
					logging.debug('Inserting new record')
					self.insertResource(type, title, linkOrAddress, desc)
			except:
				logging.error('updateResource failed')
		
	#delete
	@classmethod
	def deleteAllResources(self):
		try:
			resource_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(resource_keys)
			logging.debug('deleteAllResources success')
		except:
			logging.error('deleteAllResources failed')
						
	@classmethod	
	def deleteResourceByID(self, id):
			try:
			
				if(id != 'None'):
					delete_resource = Resource.get_by_id(int(id))
					delete_resource.key.delete()
					logging.debug('deleteResourceByID success')
			except:
				logging.error('deleteResourceByID failed')	