from django.shortcuts import render
from .models import ContactInfo


def index(request):
    services = ContactInfo.objects.filter(is_visible=True)
    context = {
        'services': services,
    }
    return render(request, 'service.html', context=context)
