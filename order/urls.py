from django.urls import path
from . import views

urlpatterns = [
    # path('', views.orders_open),
    # path('orders', views.orders_auth),
    path ('create_order', views.create_order, name = 'create'),
    path ('delete_order', views.delete_order, name = 'delete'),
    path('my_orders', views.show_my_orders, name = 'show_my_orders'),
    path ('', views.show_all_orders, name = 'show_all_orders'),





]