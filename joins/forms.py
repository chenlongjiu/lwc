# getting a form
from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField(required = True)