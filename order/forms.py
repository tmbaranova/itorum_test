from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
from .models import Order
import datetime

class OrderForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=User.objects.filter(role='customer'))
    order_date = forms.DateField()
    class Meta:
        model = Order
        fields = ['price', 'customer', 'order_date']


class OrderDateForm(forms.Form):
    now = datetime.date.today()
    first_day_of_month = now - datetime.timedelta(days=now.day)
    d = now
    lst = []
    # while d >=first_day_of_month:
    #     if d.weekday == 1:
    #         lst.append(d)
    #     d + datetime.timedelta(days=1)




    # weeks = forms.ChoiceField(choices=None)