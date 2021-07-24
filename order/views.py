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
from django.db.models import Sum, Count
import json
from django.db.models.functions import TruncDay, TruncDate

User = get_user_model()

@login_required
def create_order(request):

    if request.is_ajax():
        form = OrderForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
            form.save()
            orders = Order.objects.all().order_by('-order_date')
            return render(request, 'auth_orders.html', {'form': form, 'orders': orders})
        orders = Order.objects.all().order_by('-order_date')
        return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

    orders = Order.objects.all().order_by('-order_date')
    form = OrderForm()
    return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect("orders:create")

def get_data_for_week(monday, sunday):
    data_for_week = {}
    orders_current_week2 = Order.objects.filter(order_date__gte=monday).filter(
        order_date__lte=sunday)
    print (orders_current_week2)
    orders_current_week = Order.objects.filter(order_date__gte=monday).filter(
        order_date__lte=sunday).values('order_date').annotate(
        day_sum=Sum('price'),
        customers=Count('customer', distinct=True)
    ).order_by('-order_date')
    print (orders_current_week)
    data_for_week['orders_current_week'] = orders_current_week


    week_sum = orders_current_week.aggregate(
        week_sum=Sum('day_sum')
    )
    data_for_week['week_sum'] = week_sum['week_sum']

    week_customers = User.objects.filter(orders__order_date__gte=monday).filter(
        orders__order_date__lte=sunday).distinct()



    data_for_week['week_customers'] = week_customers
    return data_for_week


def show_all_orders(request):

    if request.is_ajax():
        form = OrderDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['weeks']
            monday, sunday = date.split(' - ')
            monday = datetime.datetime.strptime(monday, '%d.%m.%Y')
            sunday = datetime.datetime.strptime(sunday, '%d.%m.%Y')
            data_for_week = get_data_for_week(monday, sunday)
            return render(request, 'all_orders.html',
                          {'data_for_week': data_for_week, 'form': form})

        return render(request, 'all_orders.html',
                      {'form': form})

    now = datetime.date.today()
    monday = now - datetime.timedelta(days=now.weekday())
    sunday = monday + datetime.timedelta(days=6)
    data_for_week = get_data_for_week(monday, sunday)
    form = OrderDateForm()
    return render(request, 'all_orders.html', {'data_for_week':data_for_week, 'form':form, })

