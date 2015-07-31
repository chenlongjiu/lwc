from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join
# Create your views here.

def home(request):
	#print request.POST
	#using django form method 
	# form = EmailForm(request.POST)
	# if form.is_valid():
	# 	email =  form.cleaned_data['email']
	# 	new_join , create = Join.objects.get_or_create(email = email)
	# 	print new_join, create
	# 	if create: 
	# 		print Created

	#this is using model forms
	form = JoinForm(request.POST or None)
	if form.is_valid:
		#new_join = form.save(commit=False)
		email =  form.cleaned_data['email']
		new_join2 , create = Join.objects.get_or_create(email = email)
		#new_join.save() #ok with duplicate
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
