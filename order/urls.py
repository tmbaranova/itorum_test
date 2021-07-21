from django.urls import path
from . import views

urlpatterns = [
    # path('', views.orders_open),
    # path('orders', views.orders_auth),
    path('sign_up', views.SignUp.as_view(), name='signup'),

]