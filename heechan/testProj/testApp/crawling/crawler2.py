from bs4 import BeautifulSoup
import requests

def crawler2():
  r = requests.get("https://freemusicarchive.org/static")
  html = r.text
  soup = BeautifulSoup(html, 'html.parser')

  my_titles = soup.select('a.icn-arrow')
  arr = []
  for title in my_titles:
      arr.append(title.get('href'))
  
  return arr