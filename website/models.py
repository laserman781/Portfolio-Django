from django.db import models

# Create your models here.
class Experience(models.Model):
	# Images
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	#image = models.ImageField(upload_to='/images/', null=True)
	# Summary
	summary = models.TextField()

class Awards(models.Model):
	#Title
	titledate = models.CharField(max_length=200)
	#description
	#image = models.ImageField(upload_to='images/', null=True)
	description = models.TextField()

class Leadership(models.Model):
	#Title
	titledate = models.CharField(max_length=200)
	#image = models.ImageField(upload_to='images/', null=True)
	#description
	description = models.TextField()
