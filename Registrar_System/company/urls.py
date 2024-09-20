from django.urls import path

from . import views
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path("home/", views.home_view, name="home"),
    #path("about/", TemplateView.as_view(template_name="about.html")),
    path('about/', views.AboutView.as_view(), name='about'),
    path("", views.index, name="index"),

    #user authentication paths
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),name='profile'),
    path("signup/", views.SignUpView.as_view(), name="templates/registration/signup"),
    path('profile/',TemplateView.as_view(template_name='profile.html'),name='profile'),
]