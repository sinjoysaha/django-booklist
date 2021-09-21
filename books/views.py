from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def book_detail_view(request, id):
    obj = get_object_or_404(Book, id=id)
    context = {
        'object': obj
    }
    return render(request, "books/book_detail.html", context)

def book_list_view(request):
    queryset = Book.objects.all() # list of objects
    context = {
        'object_list': queryset
    }
    return render(request, "books/book_list.html", context)
