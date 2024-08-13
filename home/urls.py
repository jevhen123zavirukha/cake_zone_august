from django.urls import path
from .views import index_home

app_name = 'home'

urlpatterns = [
    path('', index_home, name='home'),
]
