from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : "form-control message_inputs"}))
    contact = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : "form-control message_inputs"}))
    sometext = forms.CharField(label='', widget=forms.Textarea(attrs={'class' : "form-control message_inputs", 'rows': 5, 'cols' : 20}))