from main import *
from google.appengine.api import mail
from main import BaseHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class ContactPage(BaseHandler):
	def get(self):
		template_values ={}
		template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
		self.response.write(template.render(template_values))

	def post(self):
		notification_address = "fisher.robert26@gmail.com"
		sender_address = "<fisher.robert26@gmail.com>"
		subject = self.request.get("inputSubject")
		subject2 = "(Email from user Dancin goggin) Subject: "+subject
		name=self.request.get("inputName")
		phone=self.request.get("inputPhone")
		user_address = self.request.get("inputEmail")
		body = "\nName: "+name+"\nPhone: "+phone+"\nMessage: \n"+self.request.get("inputMessage")+"\nEmail: "+user_address
		subject_confirmation = "Confirmation, mail received."
		if subject == "Appointment":
			body_confirmation = "\nYour request for an appointment was received succesfully and an administrator will get in touch with you to plan the appointment: \n\n This is what you sent:\n Subject: "+subject+""+body
		if subject == "Shoes":
			body = "\nName: "+name+"\nPhone: "+phone+"\nMessage: \n"+self.request.get("inputMessage")+"\nShoes size: "+self.request.get("size")+"\nGender: "+self.request.get("gender")+"\nEmail: "+user_address
			body_confirmation = "\nYour request for shoes was received succesfully and an administrator will get in touch with you as soon as possible: \n\n This is what you sent:\n Subject: "+subject+""+body
		else:
			body_confirmation = "\nYour email was received succesfully and an administrator will get in touch with you as soon as possible: \n\n This is what you sent:\n Subject: "+subject+""+body
		mail.send_mail(sender_address, user_address, subject_confirmation, body_confirmation)
		algo="assignacion"
		mail.send_mail(sender_address, sender_address, subject2, body)
		self.redirect('/success')
			
		
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/contact', ContactPage)],
                              config = config, debug=True)