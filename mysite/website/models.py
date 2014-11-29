from django.db import models

# Create your models here.
class Data(models.Model):
    date=models.DateTimeField('published_time') #The time the video published.
    title=models.CharField(max_length=20000) 
    url=models.CharField(max_length=20000) #The url embed in the html.
    words=models.TextField()#The description of the video.
    def __str__(self):
        return self.title

