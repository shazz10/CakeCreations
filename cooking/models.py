

from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Recent(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=1024)
	image = models.ImageField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def save(self):
		#Opening the uploaded image
		im = Image.open(self.image)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (600,600) )

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=100)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

		super(Recent,self).save()

class Activity(models.Model):
	title = models.CharField(max_length=70)
	image = models.ImageField()
	created = models.DateTimeField(auto_now_add=True)

	def save(self):
		#Opening the uploaded image
		im = Image.open(self.image)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (800,800) )

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=100)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

		super(Activity,self).save()


class Contact(models.Model):
	name = models.CharField(max_length=70)
	email = models.EmailField()
	message = models.TextField(max_length=2000)