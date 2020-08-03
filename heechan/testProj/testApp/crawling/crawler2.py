from bs4 import BeautifulSoup
import requests
import re

def crawler2(url):
  r = requests.get(url)
  html = r.text
  soup = BeautifulSoup(html, 'html.parser')

  my_titles = soup.select('a.icn-arrow')
  my_music = soup.select('.playtxt .ptxt-artist')
  my_artist = soup.select('.playtxt .ptxt-track')

  arr = []
  music_title = []
  music_artist= []
  for i in my_titles:
    arr.append(i.get('href'))
  for j in my_music:
    title_re = re.sub('(<([^>]+)>)',"",str(j))
    title_re  = title_re.replace('\n',"")
    music_title.append(title_re)
  for k in my_artist:
    artist_re = re.sub('(<([^>]+)>)',"",str(k))
    artist_re  = artist_re.replace('\n',"")
    music_artist.append(artist_re)
  return arr,music_title,music_artist