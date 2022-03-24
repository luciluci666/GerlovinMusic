from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : "form-control"}))
    contact = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : "form-control"}))
    sometext = forms.CharField(label='', widget=forms.Textarea(attrs={'class' : "form-control", 'rows': 5, 'cols' : 20}))