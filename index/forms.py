from django import forms





class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': 'Ivan'}))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': '8 (954) 342-11-23'}))
    mail = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class' : 'input-group__input', 'placeholder': 'adret1224@mail.ru'}))
    text = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(attrs={'class' : 'input-group__input'}))

