from google.appengine.api import users
import webapp2

class Admin(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect('/')
        else:
            users.create_login_url('/'))

 app = webapp2.WSGIApplication([
			('/admin', Admin),
			],debug=True)       