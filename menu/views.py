from django.shortcuts import render
from menu.models import Category


def index_menu(request):
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories
    }
    return render(request, 'menu.html', context=context)
