from django.urls import path,include

from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("api/", include('api.urls')),
    path('', include('django.contrib.auth.urls'))
]


