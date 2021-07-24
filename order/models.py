from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Order(models.Model):

    customer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, verbose_name='Заказчик')
    order_date = models.DateField(verbose_name='Дата') #auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')

    # class Meta:
    #     ordering = ('-order_date',)



