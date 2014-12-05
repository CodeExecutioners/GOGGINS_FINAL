from main import *
from google.appengine.api import mail
from main import BaseHandler
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)
	
class GiftPage(BaseHandler):
	def get(self):
		template_values ={}
		template = JINJA_ENVIRONMENT.get_template('templates/gift.html')
		self.response.write(template.render(template_values))
	def post(self):
		#sender_address must be gmail"
		sender_address = "fisher.robert26@gmail.com"
		subject = "Gift Certificate"
		name = self.request.get("giftInputName")
		recipient = self.request.get("giftInputRecipientName")
		email = self.request.get("giftInputEmail")
		address = self.request.get("giftInputAddress")
		city = self.request.get("giftInputCity")
		state = self.request.get("giftInputState")
		zip = self.request.get("giftInputZip")
		amount = self.request.get("giftInputAmount")
	   
		if not mail.is_email_valid(sender_address):
			# prompt user to enter a valid address
			self.redirect('/InvalidMail')
		else:
			body = name + " would like to place an order for a gift certificate in the amount of " + amount + "\n"
			body += ("The gift certificate is for " + recipient + " and is to be sent to the address:\n")
			body += ("\n" + email+ "\n" + city + " " + state + " " + zip)
			logging.debug("Gift Email Body: " + body)
			html = "<p>Test</p>"
			mail.send_mail(sender_address, email, subject, body)
			self.redirect('/success')
			
config = {}
config['webapp2_extras.sessions'] = {
	'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/gift', GiftPage)],
							  config=config,
							  debug=True)