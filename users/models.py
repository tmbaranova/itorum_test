from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.save()
        return user

    def create_superuser(self, email, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, is_superuser=True,
                          **kwargs)
        user.save()
        return user


class CustomUser(AbstractUser):

    username = models.CharField(unique=True, max_length=100,)
    made_an_order = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username', ]

    @property
    def has_made_an_order(self):
        return self.made_an_order

# Create your models here.
