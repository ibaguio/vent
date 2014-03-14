from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
	context = RequestContext(request)

	context_dict = {}
	return render_to_response('sponsors/home.html', context_dict, context)