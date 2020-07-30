from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    age = forms.IntegerField(required=False)


class PhoneForm(forms.Form):
    contact = forms.IntegerField(required=False)
    number = forms.CharField(required=True, max_length=16)
