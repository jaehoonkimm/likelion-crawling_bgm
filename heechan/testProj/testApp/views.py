from django.shortcuts import render
from .crawling import crawler2

# Create your views here.


def home(request):
    arr = crawler2.crawler2("https://freemusicarchive.org/static")
    arr1 = arr[0]
    return render(request, 'home.html', {'arr': arr,'arr1' : arr1})

def result(request):
    setting = request.GET.get('setting', '')
    url = "https://freemusicarchive.org/genre/" + setting
    arr = crawler2.crawler2(url)
    arr1 = arr[0]
    return render(request, 'home.html',{'arr': arr,'arr1' : arr1})