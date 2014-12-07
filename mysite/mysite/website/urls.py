from django.conf.urls import patterns,url

from website import views

urlpatterns=patterns('',
	url(r'^$',views.IndexView.as_view(),name='index'),
	url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),
	url(r'video$',views.VideoView.as_view(),name='video'),
	url(r'picture$',views.PictureView.as_view(),name='picture'),
	url(r'beauty$',views.BeautyView.as_view(),name='beauty'),
	url(r'(?P<data_id>\d+)/comment/$',views.comment,name='comment'),
)