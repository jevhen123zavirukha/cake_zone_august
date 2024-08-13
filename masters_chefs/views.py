from django.shortcuts import render


def index_masters(request):
    return render(request, 'masters.html')
