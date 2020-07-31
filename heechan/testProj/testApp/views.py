from django.shortcuts import render
from .crawling import crawler2
from .crawling import image

# Create your views here.


def home(request):
    arr = crawler2.crawler2("https://freemusicarchive.org/static")
    arr1 = arr[0]
    images = image.url_get()
    image1 = images[0]
    return render(request, 'home.html', {'arr': arr,'arr1' : arr1, 'genre': 'static', 'images' : images, 'image1' : image1})

def result(request):
    setting = request.GET.get('setting', '')
    url = "https://freemusicarchive.org/genre/" + setting
    arr = crawler2.crawler2(url)
    arr1 = arr[0] if arr else ''
    images = image.url_get(setting)
    image1 = images[0]

    return render(request, 'home.html',{'arr': arr,'arr1' : arr1, 'genre': setting, 'images' : images, 'image1' : image1})