from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('order_list', views.order_list, name='order_list'),
    ]
