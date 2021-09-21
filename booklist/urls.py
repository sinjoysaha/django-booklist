"""booklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, about_view, contact_view

admin.site.site_header = 'BookList Admin'
admin.site.site_title = 'BookList Admin Portal'
admin.site.index_title = 'Welcome to BookList Admin'

urlpatterns = [
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    #path('books/', books_view, name='books'),
    # path('', include('pages.urls')),
    # path('', 'index.html', name='home'),
]
