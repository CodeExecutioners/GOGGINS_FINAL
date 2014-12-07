import webapp2
from google.appengine.ext import ndb

class Lesson(ndb.Model):
	"""Models an individual lesson"""
	city = ndb.StringProperty()
	#datetime = ndb.DateTimeProperty()
	location = ndb.StringProperty()
	cost = ndb.FloatProperty()
	