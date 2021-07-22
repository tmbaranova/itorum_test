from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import OrderForm
from .models import Order

User = get_user_model()

@login_required
def create_order(request):
    orders = Order.objects.filter(customer = request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect("orders:show_my_orders")

        return render(request, 'my_orders.html', {'form': form, 'orders': orders})

    form = OrderForm()
    return render(request, 'my_orders.html', {'form': form, 'orders': orders})

@login_required
def delete_order(request, username, order_id):
    order = get_object_or_404(Order, id=order_id, author__username=username)
    if request.user != order.customer:
        return redirect('posts:post', username=username, post_id=order_id)
    order.delete()
    return redirect('posts:index')


@login_required
def show_my_orders(request):
    orders = Order.objects.filter(customer = request.user)
    form = OrderForm()

    return render(request, 'my_orders.html', {'form': form, 'orders': orders})


def show_all_orders(request):
    all_orders = Order.objects.all()
    return render(request, 'my_orders.html', {'orders':
                                              all_orders})