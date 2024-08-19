from django.shortcuts import render, redirect
from .models import ContactInfo
from .forms import MessageFromCustomerForm, SubscriberForm


def index(request):
    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')

        context = {
            'message_form': form,
            'contacts': ContactInfo.objects.first()
        }
        return render(request, 'contact.html', context=context)
    else:
        context = {
            'message_form': MessageFromCustomerForm(),
            'contacts': ContactInfo.objects.first()
        }
        return render(request, 'contact.html', context=context)


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = SubscriberForm()

    return render(request, 'contact.html', {'subscriber_form': form})
