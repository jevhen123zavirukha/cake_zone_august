from django.urls import path
from .views import index

app_name = 'masters_chefs'

urlpatterns = [
    path('', index, name='masters_chefs'),
]
