# getting a form
from django import forms
from .models import Join

class EmailForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField(required = True)


class JoinForm(forms.ModelForm):
	class Meta:
		model = Join