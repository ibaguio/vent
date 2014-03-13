from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.template import RequestContext
from vent.forms import AuthenticationForm
from vent.models import User, Organization

def homepage(request):
   return render(request,"homepage-all.html",{})

def login(request):
   """
   Log in view
   """
   if request.user.is_authenticated():
      return redirect('/home')

   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
         user = authenticate(username=request.POST['username'], password=request.POST['password'])
         if user is not None:
            if user.is_active:
               django_login(request, user)
               return redirect('/home')
   else:
      form = AuthenticationForm()
   return render(request,'login.html', {'form': form}, context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/login')


def home():
	pass

def about(request):
	return render(request,"about/about.html")

def supportUs(request):
	return render(request,"about/support-us.html")

def faq(request):
	return render(request,"about/faq.html")

def contact(request):
	return render(request,"about/contact.html")