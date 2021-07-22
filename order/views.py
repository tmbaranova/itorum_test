from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import OrderForm
from .models import Order
from django.http import HttpResponse
from users.forms import UserCreationForm

User = get_user_model()

@login_required
def create_order(request):
    orders = Order.objects.all()
    if request.method == 'POST' and request.is_ajax():
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect("orders:show_auth_orders")

        return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

    form = OrderForm()
    return render(request, 'auth_orders.html', {'form': form, 'orders': orders})

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect("orders:show_auth_orders")


@login_required
def show_auth_orders(request):
    orders = Order.objects.all()
    form = OrderForm()

    return render(request, 'auth_orders.html', {'form': form, 'orders': orders})


def show_all_orders(request):
    all_orders = Order.objects.all()
    return render(request, 'all_orders.html', {'orders':
                                              all_orders})


def hello(request):
    return HttpResponse('Hello')