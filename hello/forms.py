from django import forms
from .models import Friend, Message

class HelloForm(forms.Form):
    name = forms.CharField(label='Name', \
                           widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='Email', \
                           widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender', required=False, \
                                widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label='Age', \
                             widget=forms.NumberInput(attrs={'class':'form-control'}))
    # id = forms.IntegerField(label='ID')
    birthday = forms.DateField(label='Birth', \
                               widget=forms.DateInput(attrs={'class':'form-control'}))

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']


class SessionForm(forms.Form):
    session = forms.CharField(label='session', required=False, \
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
                           widget=forms.TextInput(attrs={'class':'form-control'}))

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':2}),
            'friend': forms.Select(attrs={'class':'form-control form-control-sm'}),
        }