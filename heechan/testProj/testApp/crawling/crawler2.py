from bs4 import BeautifulSoup
import requests

def crawler2(url):
  r = requests.get(url)
  html = r.text
  soup = BeautifulSoup(html, 'html.parser')

  my_titles = soup.select('a.icn-arrow')
  arr = []
  for title in my_titles:
      arr.append(title.get('href'))
  
  return arr