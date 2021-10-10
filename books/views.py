from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

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

def book_create_view(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        obj_saved = form.save()
        return redirect(f'../{obj_saved.id}/')

    context = {
        'title': 'New Book',
        'form': form
    }
    return render(request, "books/book_create.html", context)

def book_update_view(request, id=id):
    obj = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')

    context = {
        'title': 'Edit Book',
        'form': form
    }
    return render(request, "books/book_create.html", context)

def book_delete_view(request, id):
    obj = Book.objects.get(id=id)
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')

    context = {
        'object': obj
    }
    return render(request, "books/book_delete.html", context)