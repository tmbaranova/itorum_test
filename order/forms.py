from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
from .models import Order

class OrderForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=User.objects.exclude(orders=None))
    class Meta:
        model = Order
        fields = ['price', 'customer']