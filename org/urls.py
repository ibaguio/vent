from django.conf.urls import patterns, url
from org import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'))