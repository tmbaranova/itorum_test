from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
import datetime
from .models import Order

User = get_user_model()


class OrderForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=User.objects.filter(
        role='customer'), label='Заказчик')
    order_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}), label='Дата')

    class Meta:
        model = Order
        fields = ['price', 'customer', 'order_date']


def get_weeks():
    now = datetime.date.today()
    first_day_of_month = now - datetime.timedelta(days=(now.day - 1))
    weeks_str = []
    while now >= first_day_of_month:
        if now.weekday() == 0:
            monday_str = now.strftime('%d.%m.%Y')
            sunday_str = (now+datetime.timedelta(days=6)).strftime('%d.%m.%Y')
            week = f'{monday_str} - {sunday_str}'
            weeks_str.append((week, week))

        now -= datetime.timedelta(days=1)
    return weeks_str


class OrderDateForm(forms.Form):
    weeks = forms.ChoiceField(choices=get_weeks(), label='Неделя')
