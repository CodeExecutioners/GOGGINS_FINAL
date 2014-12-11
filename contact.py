from main import *
from google.appengine.api import mail
from main import BaseHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class ContactForm(BaseHandler):
	def get(self):
		logging.debug("Contact Form GET")
		template_values= {}
		template = JINJA_ENVIRONMENT.get_template('templates/contact_form.html')
		self.response.write(template.render(template_values))
		

class ContactPage(BaseHandler):
	def get(self):
		user = self.session.get('user')
		template_values ={'user': user}
		template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
		self.response.write(template.render(template_values))

	def post(self):
		notification_address = "fisher.robert26@gmail.com"
		sender_address = "<fisher.robert26@gmail.com>"
		subject = self.request.get("inputSubject")
		subject_for_goggins = subject
		name=self.request.get("inputName")
		phone=self.request.get("inputPhone")
		user_address = self.request.get("inputEmail")
		message = self.request.get("inputMessage")
		
		
		subject_confirmation = "Goggin Ballroom Dancing: Contact Request Confirmation."
		if subject == "Shoes":
			size = self.request.get('size')
			gender = self.request.get('gender')
			clientbody = ("""
Dear """+name+""",

Thank you for contacting Goggin Ballroom Dancing.

This is your contact request information:

	Name: """+name+"""
	Subject: """+subject+"""
	Gender: """ + gender + """
	Size: """ + size + """
	Phone: """ + phone+"""
	Email: """ + user_address+"""
	Message: """ +message+ """

We will contact you as soon as possible.

Sincerely,

Dave & Karen Goggin
715.833.1879
Email@DancinGoggin.com
Goggin Ballroom Dancing""")


			gogginsBody = ("""
Dear Dave & Karen,

You have received a contact request:

	Name: """+name+"""
	Subject: """+subject+"""
	Gender: """ + gender + """
	Size: """ + size + """
	Phone: """ + phone+"""
	Email: """ + user_address+"""
	Message: """ +message+ """

A confirmation message has been sent to the contact's email.

From,

DancinGoggin.com
""")





		else:
			clientbody = ("""
Dear """+name+""",

Thank you for contacting Goggin Ballroom Dancing.

This is your contact request information:

	Name: """+name+"""
	Subject: """+subject+"""
	Phone: """ + phone+"""
	Email: """ + user_address+"""
	Message: """ +message+ """

We will contact you as soon as possible.

Sincerely,

Dave & Karen Goggin
715.833.1879
Email@DancinGoggin.com""")
			gogginsBody = ("""
Dear Dave & Karen,

You have received a contact request:

	Name: """+name+"""
	Subject: """+subject+"""
	Phone: """ + phone+"""
	Email: """ + user_address+"""
	Message: """ +message+ """
	
A confirmation message has been sent to the contact's email.

From,

DancinGoggin.com
""")






		#send message to client
		mail.send_mail(sender_address, user_address, subject_confirmation, clientbody)
		
		#send mail to goggins
		mail.send_mail(sender_address, sender_address, subject, gogginsBody)
		self.redirect('/contact')
	
		
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/contact', ContactPage),('/contactForm', ContactForm) ],
                              config = config, debug=True)