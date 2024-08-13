from django.urls import path
from .views import index_menu

app_name = 'menu'

urlpatterns = [
    path('', index_menu, name='index'),
]
