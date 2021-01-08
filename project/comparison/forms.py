from django import forms

from .models import RegexValidator
class Form(forms.Form):
   username = forms.CharField(max_length=40 , validators=[RegexValidator])