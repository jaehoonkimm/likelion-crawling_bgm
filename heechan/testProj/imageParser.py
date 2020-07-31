# server run 없이 단독으로 django 구동 가능하도록 하는 코드
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testProj.settings")
import django
django.setup()

import requests
from bs4 import BeautifulSoup as bs
import json

from imageCrawler.models import ImageData

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def url_get(keyword="coffee"):
    URL = "https://unsplash.com/s/photos/%s?orientation=landscape" %keyword
    response = requests.get(URL)
    html = response.text
    soup = bs(html, 'html.parser')

    photoURL_ls = []

    cnt = 0
    for i in soup.select('div.nDTlD'):
        for j in str(i).split():
            if j.startswith('href="/photos/'):
                innerURL = "https://unsplash.com"+j.replace('href="','').replace('"','')
                innerResponse = requests.get(innerURL)
                innerhtml = innerResponse.text
                innerSoup = bs(innerhtml, 'html.parser')
                temp = innerSoup.select('div._2yFK-.IEpfq > img._2zEKz[src]')
                for url in temp:
                    photoURL_ls.append(url['srcset'].split("w,")[8])
        cnt = cnt+1
        if(cnt==20):
            break
    return photoURL_ls

if __name__=='__main__':
    dict_image_data = url_get()
    for link in dict_image_data:
        ImageData(image_link = link).save()
                

            

