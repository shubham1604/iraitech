from django import forms

class MyForm(forms.Form):
    x = forms.IntegerField()
    n = forms.IntegerField()
