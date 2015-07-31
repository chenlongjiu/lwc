from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join
# Create your views here.

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x.x_forward.split(',')[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except exp:
		print "exception: " + exp
		ip = ""
	return ip



def home(request):
	print request.META.get('REMOTE_ADDR')
	print request.META.get("HTTP_X_FORWARDED_FOR")
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
	if form.is_valid():
		new_join = form.save(commit=False)
		#email =  form.cleaned_data['email']
		#new_join2,create  = Join.objects.get_or_create(email = email)
		new_join.ip_address = get_ip(request)
		new_join.save() #ok with duplicate
	context = {"form":form}
	template = "home.html"
	return render(request, template, context)
