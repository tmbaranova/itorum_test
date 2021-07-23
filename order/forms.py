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
    first_day_of_month = now - datetime.timedelta(days=(now.day - 1))

    d = now
    lst = []
    lst2=[]
    while d >= first_day_of_month:
        print(d)
        print(d.weekday())
        if d.weekday() == 0:
            lst.append((1,d))
            lst2.append((1,d+datetime.timedelta(days=6) ))
        d -= datetime.timedelta(days=1)

    print(lst)
    print (lst2)




    monday = forms.ChoiceField(choices=lst)
    sunday = forms.ChoiceField(choices=lst2)