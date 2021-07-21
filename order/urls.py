from django.urls import path
from . import views

urlpatterns = [
    # path('', views.orders_open),
    # path('orders', views.orders_auth),
    path ('create_order', views.create_order)


]