from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create_order', views.create_order, name='create'),
    path('<int:order_id>/delete_order', views.delete_order, name='delete'),
    path('auth_orders', views.create_order, name='create'),
    path('', views.show_all_orders, name='show_all_orders'),
]