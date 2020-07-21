from django.shortcuts import render
from .crawling import crawler2

# Create your views here.


def home(request):
    arr = crawler2.crawler2()
    
    return render(request, 'home.html', {'arr': arr})
