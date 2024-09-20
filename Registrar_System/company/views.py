from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to Company Django App.")

def home_view(request): #function-based view that displays a simple message
    return HttpResponse("Welcome to ABC's University Registrar System.")

class AboutView(TemplateView): #class-based view that renders a template
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Alice'
        context['age'] = 30
        context['items'] = ['apple', 'banana', 'orange']
        context['my_data'] = 'This is data passed to the template'
        return context

#Views used for authentications
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"