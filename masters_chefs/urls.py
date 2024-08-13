from django.urls import path
from .views import index_masters

app_name = 'master_chefs'

urlpatterns = [
    path('', index_masters, name='master_chefs'),
]
