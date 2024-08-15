from django.shortcuts import render
from .models import Service


def index(request):
    categories = Service.objects.filter(is_visible=True)
    context = {
        'categories': categories,
    }
    return render(request, 'service.html', context=context)
