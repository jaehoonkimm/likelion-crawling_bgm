from django.shortcuts import render
from .crawling import crawler
from .crawling import crawler2
from .crawling import crawler3
from .crawling import image
import re

# Create your views here.


def home(request):
    arr,title,artist = crawler3.crawler3("https://freemusicarchive.org/static")
    arr1,title1,artist1 = arr[0],title[0],artist[0]
    images = image.url_get()
    image1 = images[0]
    return render(request, 'home.html', {'arr': arr,'arr1' : arr1, 'genre': 'static', 'images': images, 'image1': image1,'title':title,'title1':title1,'artist':artist,'artist1':artist1})

def result(request):
    setting = request.GET.get('setting', '')
    url = "https://freemusicarchive.org/genre/" + setting
    arr,title,artist = crawler2.crawler2(url)
    
    arr1 = arr[0] if arr else ''
    atitle1,artist1 = title[0],artist[0]
    
    images = image.url_get(setting)
    image1 = images[0]

    return render(request, 'home.html',{'arr': arr,'arr1' : arr1, 'genre': setting, 'images': images, 'image1': image1,'title':title,'title1':title1,'artist':artist,'artist1':artist1})