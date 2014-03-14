from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('vent.views',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', include('vcalendar.urls'), name='home'),
   url(r'^login/$','login'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^home/$','home'),
   url(r'^about/$','about'),
   url(r'^support-us/$','supportUs'),
   url(r'^faq/$','faq'),
   url(r'^contact-us/$','contact'),
   url(r'^logout/$', 'logout', name='logout'),
   url(r'^calendar/$', include('vcalendar.urls'), name='vcalendar'),
   url(r'^event/$', include('event.urls'), name='event'),
   url(r'^org/$', include('org.urls'), name='org'),
   url(r'^sponsors/$', include('sponsors.urls'), name='sponsors'),
)
