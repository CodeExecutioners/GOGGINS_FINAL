from main import *
from main import BaseHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class SuccessPage(BaseHandler):
   def get(self):
		resources = models.Resource.getAllResources()
		users = self.session.get('user')
		template_values ={'user':users, 'resources': resources}
		template = JINJA_ENVIRONMENT.get_template('templates/success.html')
		self.response.write(template.render(template_values))
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/success', SuccessPage)],
                              config=config,debug=True)
