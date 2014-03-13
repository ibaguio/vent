from django.conf.urls import patterns, url
from vcalendar import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'))