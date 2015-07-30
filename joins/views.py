from django.shortcuts import render

from .forms import EmailForm
from .models import Join
# Create your views here.

def home(request):
	#print request.POST
	form = EmailForm(request.POST)
	if form.is_valid():
		email =  form.cleaned_data['email']
		new_join , create = Join.objects.get_or_create(email = email)
		print new_join, create
		if create: 
			print "Created"
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
