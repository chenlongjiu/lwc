# function class based use
#there's a request 
from django.shortcuts import render

def home(request):
	context = {}
	template = "home.html"
	return render(request, template, context)