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
    # now = datetime.date.today()
    # first_day_of_month = now - datetime.timedelta(days=(now.day-1))
    #
    # d = now
    # lst = []
    # while d >= first_day_of_month:
    #     print (d)
    #     print (d.weekday())
    #     if d.weekday() == 0:
    #         lst.append((d,d + datetime.timedelta(days=6) ))
    #     d -= datetime.timedelta(days=1)
    #
    # print(lst)
    #
    #
    # if date:
    #     monday = date - datetime.timedelta(days=date.weekday())
    # else:
    #     now = datetime.date.today()
    #     monday = now - datetime.timedelta(days=now.weekday())
    #
    # sunday = monday + datetime.timedelta(days=6)
    # orders_current_week = Order.objects.filter(order_date__gte=monday).filter(order_date__lte=sunday)
    all_orders = Order.objects.all()
    form = OrderDateForm()
    return render(request, 'all_orders.html', {'orders':all_orders, 'form':form})


def hello(request):
    return HttpResponse('Hello')