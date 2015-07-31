# getting a form
from django import forms
from .models import Join

class EmailForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField(required = True)


class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ["email"]#which field need to show
		#exclude = [] #which field you don't need