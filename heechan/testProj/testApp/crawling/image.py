import requests
from bs4 import BeautifulSoup as bs

def url_get(keyword="coffee"):
    URL = "https://unsplash.com/s/photos/%s?orientation=landscape" %keyword
    response = requests.get(URL)
    html = response.text
    soup = bs(html, 'html.parser')

    tempURL_ls = []
    photoURL_ls = []

    for i in soup.select('div.nDTlD'):
        for j in str(i).split():
            if 'href' in j and j.startswith('href="/photos/'):
                innerURL = "https://unsplash.com"+j.replace('href="','').replace('"','')
                innerResponse = requests.get(innerURL)
                innerhtml = innerResponse.text
                innerSoup = bs(innerhtml, 'html.parser')
                temp = innerSoup.select('div._2yFK-.IEpfq > img._2zEKz')
                for idx, z in enumerate(temp):
                    tempURL_ls.append(z['srcset'].split())
                    photoURL_ls.append(tempURL_ls[-1][-2])
                    tempURL_ls = []
                    
    photoURL_ls = set(photoURL_ls)
    photoURL_ls = list(photoURL_ls)
    return photoURL_ls