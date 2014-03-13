from django import forms
from django.contrib import admin
from vent.models import User, Organization

admin.site.register(User)
admin.site.register(Organization)

