from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    mail = forms.CharField(max_length=200, required=False)
    text = forms.CharField(max_length=1000, required=False)