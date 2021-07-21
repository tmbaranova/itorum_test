from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "made_an_order", "username")


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
