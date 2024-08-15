from django.shortcuts import render
from .models import Establishment


def index(request):
    home = Establishment.objects.filter(is_visible=True)
    context = {
        'home': home,
    }
    return render(request, 'home.html', context=context)
