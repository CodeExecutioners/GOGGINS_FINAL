from main import *
from google.appengine.api import mail
from main import BaseHandler
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)
	
class GiftPage(BaseHandler):
	def get(self):
		resources = models.Resource.getAllResources()
		users = self.session.get('user')
		template_values ={'user':users, 'resources': resources}
		template = JINJA_ENVIRONMENT.get_template('templates/gift.html')
		self.response.write(template.render(template_values))
	def post(self):
		#sender_address must be gmail"
		sender_address = "<fisher.robert26@gmail.com>"
		subject = "Goggin Ballroom Dancing: Gift Certificate"
		name = self.request.get("giftInputName")
		recipient = self.request.get("giftInputRecipientName")
		phone = self.request.get("giftInputPhone")
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
			clientbody = ("""
Dear """+name+""",

Thank you for contacting Goggin Ballroom Dancing.

This is your gift certificate order information:

	Name: """+name+"""
	Recipient's Name: """+recipient+"""
	Phone: """ + phone+"""
	Email: """ + email+"""
	Street Address: """+address+"""
	City: """ +city+"""
	State: """+ state +"""
	Zip Code: """ + zip + """
	Dollar Amount: """ + amount +"""

To receive your gift certificate, please send your check or money order to the following address:

	Dave & Karen Goggin
	1718 Delrae Ct
	Eau Claire, WI 54703

Once we recieve your mailed order, we will then send the gift certificate to you by mail as soon as possible.

Sincerely,

Dave & Karen Goggin
715.833.1879
Email@DancinGoggin.com
Goggin Ballroom Dancing""")


			gogginsBody = ("""
Dear Dave & Karen,

You have received a gift certificate order:

	Name: """+name+"""
	Recipient's Name: """+recipient+"""
	Phone: """ + phone+"""
	Email: """ + email+"""
	Street Address: """+address+"""
	City: """ +city+"""
	State: """+ state +"""
	Zip Code: """ + zip + """
	Dollar Amount: """ + amount +"""

A confirmation message has been sent to the contact's email. The email has informed the contact to send a check or money order by mail to the following address:

	Dave & Karen Goggin
	1718 Delrae Ct
	Eau Claire, WI 54703

You should be expecting a mailed gift certificate order soon.
	
From,

DancinGoggin.com
""")

		
			
		#send message to client
		mail.send_mail(sender_address, email, subject, clientbody)
		logging.debug("sent Contact Gift Certificate's email")
		#send mail to goggins
		mail.send_mail(sender_address, sender_address, subject, gogginsBody)
		logging.debug("sent Goggin's Gift Certificate's email")
		self.redirect('/gift')
			
config = {}
config['webapp2_extras.sessions'] = {
	'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([('/gift', GiftPage)],
							  config=config,
							  debug=True)