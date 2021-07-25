from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.save()
        return user

    def create_superuser(self, email, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=True, is_superuser=True,
                          **kwargs)
        user.save()
        return user


class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    USER = 'user'
    USER_TYPE_CHOICES = (
        (CUSTOMER, 'customer'),
        (USER, 'user'),
    )
    role = models.CharField(max_length=100, choices=USER_TYPE_CHOICES,
                            default='user', verbose_name='Роль')
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=100,
                                verbose_name='Имя пользователя')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username', ]

    @property
    def is_customer(self):
        return self.role == 'customer'
