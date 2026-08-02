from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ism')
    phone = forms.CharField(max_length=20, label='Telefon raqam')
    message = forms.CharField(widget=forms.Textarea, label='Xabar')
