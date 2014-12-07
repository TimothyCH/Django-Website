from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from website.models import Data,Url,Comments


class IndexView(generic.ListView):
	template_name='website/index.html'
	context_object_name='data_list'
	def get_queryset(self):
		return Data.objects.order_by('-date')[:25]
		
class DetailView(generic.DetailView):
	model=Data
	template_name='website/detail.html'
	
class VideoView(generic.ListView):
	template_name='website/index.html'
	context_object_name='data_list'
	def get_queryset(self):
		v_list=Data.objects.filter(vtag=True)
		return v_list
		
class PictureView(generic.ListView):
	template_name='website/index.html'
	context_object_name='data_list'
	def get_queryset(self):
		p_list=Data.objects.filter(ptag=True)
		return p_list

class BeautyView(generic.ListView):
	template_name='website/index.html'
	context_object_name='data_list'
	def get_queryset(self):
		b_list=Data.objects.filter(btag=True)
		return b_list
		
		
def is_email(str):#judge if a str is an email.
	import re
	if re.match('\w+@\w+.\w+',str):
		return True
	else:
		return False
	
	
		
def comment(request,data_id):
	data=get_object_or_404(Data,pk=data_id)
	comment_name=request.POST['name']
	comment_email=request.POST['email']
	comment_text=request.POST['text']
	if not is_email(comment_email):
		return render(request,'Please input a real email address!')
	if not comment_name:
		return render(request,'Please enter an valid user name.')
	comment=Comments()
	comment.name=comment_name
	comment.email=comment_email
	comment.text=comment_text
	comment.date=timezone.now()
	comment.data=data
	comment.save()
	return HttpResponseRedirect(reverse('website:detail',args=(data.id,)))
	