from django.forms import ModelForm, forms
from cooking.models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class' : 'form-control','placeholder':"Your Name",'label':''})
		self.fields['email'].widget.attrs.update({'class' : 'form-control','placeholder':"Your Email"})
		self.fields['message'].widget.attrs.update({'class' : 'form-control','placeholder':"Your Message"})