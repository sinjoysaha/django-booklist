from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title         = models.CharField(max_length=120) # max_length = required
    author        = models.CharField(max_length=120)
    avg_rating    = models.DecimalField(decimal_places=2, max_digits=3)
    isbn          = models.CharField(max_length=10, blank=True)
    isbn13        = models.CharField(max_length=13)
    lang          = models.CharField(max_length=20)
    num_pages     = models.IntegerField()
    ratings_count = models.IntegerField()
    reviews_count = models.IntegerField()
    pub_date      = models.DateField()
    publisher     = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("books:book-detail", kwargs={"id": self.id}) # f"/books/{self.id}/"  