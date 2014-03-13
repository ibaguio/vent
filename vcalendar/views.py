from django.template import RequestContext
from django.shortcuts import render_to_response
import json
import random

def home(request):
	context = RequestContext(request)

	# Generate dummy 30-day data

	dayHasEvent = []
	for i in range(0,30):
		dayHasEvent.append(False)

	for i in range(0,5):
		dayHasEvent[random.randrange(0,30,1)] = True

	weekDays = ['Su', 'M', 'T', 'W', 'Th', 'F', 'Sa', 'Su', 'M', 'T', 'W', 'Th', 'F', 'Sa', 'Su', 'M', 'T', 'W', 'Th', 'F', 'Sa', 'Su', 'M', 'T', 'W', 'Th', 'F', 'Sa', 'Su', 'M']

	context_dict = { 'dayHasEvent' : json.dumps(dayHasEvent), 'weekDays' : json.dumps(weekDays) }

	return render_to_response('calendar/home.html', context_dict, context)