from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Book
from .models import student
# Create your views here.


def index(request):
    return HttpResponse("Hello, Welcome to the Admission page.")

def hello_view(request):
    return HttpResponse("Hello World!")
def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'book_list.html', context)

class HelloView(TemplateView):
    """A class-based view rendering a template named 'hello.html'."""
    template_name = 'hello.html'

class BookDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Book
  template_name = 'books/book_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() #assuming a method get_average_rating exists on the Book model

class StudentList(TemplateView):
    template_name = 'student_list.html'
    model = student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = student.objects.all()
        context = {'student_list': students}
        return context
