from django.urls import path
from .views import index

app_name = 'our_service'

urlpatterns = [
    path('', index, name='services'),
]
