from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls', namespace='api')),
    path('accounts/', include('users.urls', namespace='users')),
    path('', include('order.urls', namespace='orders')),
]
