from bs4 import BeautifulSoup
import requests
import re

def crawler3(url):
  r = requests.get(url)
  html = r.text
  soup = BeautifulSoup(html, 'html.parser')

  my_titles = soup.select('a.icn-arrow')
  my_music = soup.select('.playtxt a')
  arr = []
  music_title = []
  music_artist= []
  flag = True
  for title in my_titles:
      arr.append(title.get('href'))
  for j in my_music:
    title_re = re.sub('(<([^>]+)>)',"",str(j))
    if flag:
        music_title.append(title_re)
    else:
        music_artist.append(title_re)
    flag = not flag
  return arr,music_title,music_artist