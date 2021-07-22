from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "role")