from django.urls import include, path

from . import views

app_name = 'users'

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("api/", include('api.urls')),
    path('', include('django.contrib.auth.urls'))
]
