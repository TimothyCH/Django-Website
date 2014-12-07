import sys
import os
sys.path.append('E:/websiteProj/mysite')
os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
from website.models import Data,Url
from django.utils import timezone
if __name__=='__main__':
	import django  
	django.setup()
	d1=Data.objects.get(title="testd2")
	u1=Url()
	u1.text="www.test2.com"
	u1.data=d1
	u1.save()
	# d2=Data()
	# d2.title="testd2"
	# d2.text="this is d2"
	# d2.atag=True
	# d2.date=timezone.now()
	# d2.save()