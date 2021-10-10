from django import forms
from django.db import models
from django.db.models import fields

from .models import Book

class BookForm(forms.ModelForm):
    title         = forms.CharField(max_length=120,
                                    label='Title') 
    author        = forms.CharField(max_length=120,
                                    label='Author')
    avg_rating    = forms.DecimalField(decimal_places=2, max_digits=3,
                                    label='Average Rating')
    isbn          = forms.CharField(max_length=10, required=False,
                                    label='ISBN')
    isbn13        = forms.CharField(max_length=13,
                                    label='ISBN13')
    lang          = forms.CharField(max_length=20,
                                    label='Language')
    num_pages     = forms.IntegerField(label='Number of Pages')
    ratings_count = forms.IntegerField(label='Number of Ratings')
    reviews_count = forms.IntegerField(label='Number of Reviews')
    pub_date      = forms.DateField(label='Date Published', 
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'yyyy-mm-dd'}))
    publisher     = forms.CharField(max_length=120, label='Publisher')

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

    def clean_isbn(self, *args, **kwargs):
        isbn = self.cleaned_data.get("isbn")
        if not (len(isbn)==10 or len(isbn)==0):
            raise forms.ValidationError("ISBN must be of 10 digits.")
        return isbn
    
    def clean_isbn13(self, *args, **kwargs):
        isbn13 = self.cleaned_data.get("isbn13")
        if not (len(isbn13)==13  or len(isbn13)==0):
            raise forms.ValidationError("ISBN 13 must be of 13 digits.")
        return isbn13