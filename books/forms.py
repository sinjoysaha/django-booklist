from django import forms
from django.db import models
from django.db.models import fields

from .models import Book

class BookForm(forms.ModelForm):
    title         = forms.CharField(max_length=120) # max_length = required
    author        = forms.CharField(max_length=120)
    avg_rating    = forms.DecimalField(decimal_places=2, max_digits=3)
    isbn          = forms.CharField(max_length=10, required=False)
    isbn13        = forms.CharField(max_length=13)
    lang          = forms.CharField(max_length=20)
    num_pages     = forms.IntegerField()
    ratings_count = forms.IntegerField()
    reviews_count = forms.IntegerField()
    pub_date      = forms.DateField()
    publisher     = forms.CharField(max_length=120)

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'avg_rating',
            'isbn',
            'isbn13',
            'lang',
            'num_pages',
            'ratings_count',
            'reviews_count',
            'pub_date',
            'publisher',
        ]