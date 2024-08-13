from django.urls import path
from .views import index_service

app_name = 'our_service'

urlpatterns = [
    path('', index_service, name='services'),
]
