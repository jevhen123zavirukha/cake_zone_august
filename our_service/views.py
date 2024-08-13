from django.shortcuts import render


def index_service(request):
    return render(request, 'service.html')
