from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('hello/', views.hello_view, name='hello'), #mapped to the hello_view function-based view
    path('booklist/', views.book_list, name='list'), 
    #path('about/', views.HelloView.as_view(), name='about'), #pattern is mapped to the AboutView class-based view
    path('studentlist/', views.StudentList.as_view(), name='studentlist'),
]