from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

User = get_user_model()


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE,)
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('order_date',)



