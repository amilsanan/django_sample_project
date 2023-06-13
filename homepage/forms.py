from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    # password = forms.CharField(widget=forms.PasswordInput)
