from django.http import response
from django.shortcuts import render
import requests

# Create your views here.
def home_view(request):
    context = {}
    context['quotes'] = []
    context['authors'] = []

    for i in range(1, 4):
        res = requests.get("https://api.quotable.io/random")
        q = res.json()['content']
        a = res.json()['author']
        context['quotes'].append(q)
        context['authors'].append(a)
    
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html', {})

def contact_view(request):
    return render(request, 'contact.html', {})
