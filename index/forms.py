from django import forms
from django.forms import ModelForm
from .models import Order


#class OrderForm(ModelForm):
 #   class Meta:
#        model = Order
#        fields = ['order_name', 'order_phone', 'order_mail', 'order_text']
#        widgets = {
#            'order_name': forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': 'Ivan'}),
#           'order_phone': forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': '8 (954) 342-11-23'}),
#            'order_mail': forms.TextInput(attrs={'class' : 'input-group__input'}),
#            'order_text': forms.TextInput(attrs={'class' : 'input-group__input'}),
 #       }
class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': 'Ivan'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': '8 (954) 342-11-23'}))
    mail = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': 'adret1224@mail.ru'}))
    text = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(attrs={'class' : 'input-group__input'}))