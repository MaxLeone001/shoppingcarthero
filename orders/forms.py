from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
	class Meta:
	    model = Order
	    fields = ['first_name', 'last_name', 'email', 'address', 
	              'postal_code', 'city']

