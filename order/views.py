from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import OrderForm, OrderDateForm
from .models import Order
from django.http import HttpResponse, JsonResponse
from users.forms import UserCreationForm
from django.core import serializers
from django.core.serializers import serialize
import datetime

import json

User = get_user_model()

@login_required
def create_order(request):
    orders = Order.objects.all()
    if request.method == 'POST' and request.is_ajax():
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            orders = Order.objects.all()
            return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

        return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

    form = OrderForm()
    return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect("orders:show_auth_orders")



def show_all_orders(request, date=None):
    now = datetime.date.today()
    monday = now - datetime.timedelta(days=now.weekday())
    sunday = monday + datetime.timedelta(days=6)
    orders_current_week = Order.objects.filter(order_date__gte=monday).filter(order_date__lte=sunday)
    customers = []
    sum = 0
    for order in orders_current_week:
        sum += order.price
        customers.append(order.customer.username)
    customers = set(customers)

    if request.method == 'POST' or request.is_ajax():
        form = OrderDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['weeks']
            monday, sunday = date.split(' - ')
            monday = datetime.datetime.strptime(monday, '%d.%m.%Y')
            sunday = datetime.datetime.strptime(sunday, '%d.%m.%Y')
            orders_current_week = Order.objects.filter(
                order_date__gte=monday).filter(order_date__lte=sunday)

            return render(request, 'all_orders.html',
                          {'orders': orders_current_week, 'form': form, 'sum':sum, 'customers':customers})
        return render(request, 'all_orders.html',
                      {'orders': orders_current_week, 'form': form, 'sum':sum, 'customers':customers} )

    form = OrderDateForm()
    return render(request, 'all_orders.html', {'orders':orders_current_week, 'form':form, 'sum':sum, 'customers':customers})


def hello(request):
    return HttpResponse('Hello')