from django.db import models
import ast
# Create your models here.

class Data(models.Model):
	vtag=models.BooleanField(default=False) #'v' for video,'p' for picture,'a' for article.
	btag=models.BooleanField(default=False)
	ptag=models.BooleanField(default=False)
	date=models.DateTimeField('published_time') #The time we published the data.
	title=models.CharField(max_length=20000) 
	text=models.TextField()#The description of the video.
	def __str__(self):
		return self.title

class Url(models.Model):
	data=models.ForeignKey(Data)
	text=models.CharField(max_length=2000)
	is_cover=models.BooleanField(default=False)
	def __str__(self):
		return self.text

class Comments(models.Model):
	data=models.ForeignKey(Data)
	text=models.TextField()
	email=models.EmailField()
	name=models.CharField(max_length=2000)
	date=models.DateTimeField('comment_time')
	def __str__(self):
		return self.text
		
