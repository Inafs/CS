from django import forms
from django.forms import ModelForm
from .models import Order



class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['dt']

        widgets = {
            'name':forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': 'Ivan'}),
            'mail':forms.EmailInput(attrs={'class' : 'input-group__input', 'placeholder': 'adret1224@mail.ru'}),
            'phone':forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': '8 (954) 342-11-23'}),
            'text': forms.Textarea(attrs={'class' : 'input-group__input'})
        }