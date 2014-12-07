import shelve

import sys
import os
sys.path.append('E:/websiteProj/mysite')
os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
from website.models import Data,Url
from django.utils import timezone

tempbase_pos="E:/websiteProj/tempbase.dat"
def store_to_website():
#This is used to store the data from tempbase to django website database.
#We need to detact the repeat of the data before store it to django database.
	import django  
	django.setup()
	flag=False #If some data saved,turn flag to true.
	tempbase=shelve.open(tempbase_pos)
	try:
		video_list=tempbase['video']
	except KeyError:
		video_list=[]
	try:
		picture_list=tempbase['picture']
	except KeyError:
		picture_list=[]
	try:
		beauty_list=tempbase['beauty']
	except KeyError:
		beauty_list=[]
	for video in video_list:
		try:
			vtemp=Data.objects.get(title=video['title'])
		except:
			videodata=Data()
			videodata.vtag=True
			videodata.date=timezone.now()
			videodata.title=video['title']
			videodata.text=video['text']
			videodata.save()
			
			videodata=Data.objects.get(title=video['title'])
			
			url_data=Url()
			url_data.data=videodata
			url_data.text=video['url']
			url_data.save()

			flag=True
			print "Save video ",videodata.title,"successfully!"
	
	for picture in picture_list:
		try:
			pictemp=Data.objects.get(title=picture['title'])
		except:
			picdata=Data()
			picdata.ptag=True
			picdata.date=timezone.now()
			picdata.title=picture['title']
			picdata.text=picture['text']
			picdata.save()
			
			picdata=Data.objects.get(title=picture['title'])
			
			url_list=picture['url_list']
			coverflag=True
			for url in url_list:
				if coverflag:
					url.is_cover=True
					coverflag=False
				urldata=Url()
				urldata.data=picdata
				urldata.text=url
				urldata.save()
			flag=True
			print "Save picture ",picdata.title,"successfully!"
			
	for beauty in beauty_list:
		try:
			beautytemp=Data.objects.get(title=beauty['title'])
		except:
			beautydata=Data()
			beautydata.btag=True
			beautydata.date=timezone.now()
			beautydata.title=beauty['title']
			beautydata.text=beauty['text']
			beautydata.save()
			
			beautydata=Data.objects.get(title=beauty['title'])
			
			url_list=beauty['url_list']
			coverflag=True
			for url in url_list:
				if coverflag:
					url.is_cover=True
					coverflag=False
				urldata=Url()
				urldata.data=beautydata
				urldata.text=url
				urldata.save()
			flag=True
			print "Save beauty ",beautydata.title,"successfully!"
	tempbase.close()
	if flag==False:
		print "No data saved or repeated data."
if __name__=='__main__':
	store_to_website()
			
		
		