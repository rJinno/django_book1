from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')

class SessionForm(forms.Form):
    session = forms.CharField(label='session', required=False, \
                              widget=forms.TextInput(attrs={'class':'form-control'}))
