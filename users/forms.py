from django import forms

class loginForm(forms.Form):
    usr = forms.CharField()
    pwd = forms.CharField()
