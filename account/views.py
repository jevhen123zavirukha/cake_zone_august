from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class MyLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/')
