from django.shortcuts import render
from .crawling import crawler

# Create your views here.


def home(request):
    arr = crawler.crawler()
    return render(request, 'home.html', {'arr': arr})
