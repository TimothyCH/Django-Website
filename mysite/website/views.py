from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from website.models import Video

class IndexView(generic.ListView):
	template_name='website/index.html'
	context_object_name='video_list'
	def get_queryset(self):
		return Video.objects.order_by('-date')[:25]
		
class DetailView(generic.DetailView):
	model=Video
	template_name='website/detail.html'
	