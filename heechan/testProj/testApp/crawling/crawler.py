from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver


def crawler():
    url = 'https://vibe.naver.com/chart/total'

    driver = webdriver.Chrome(
        executable_path='C:/Users/Admin/Desktop/likelion-crawling_bgm/heechan/testProj/testApp/crawling/chromedriver.exe')

    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html)

    title = soup.select('.tracklist .link_text')
    rank = soup.select('.rank .text')
    singer = soup.select('tbody .artist')

    resultArr = []

    for i in range(len(title)):
        tempObj = {}
        tempObj['rank'] = rank[i].get_text()
        tempObj['title'] = title[i].attrs['title']
        tempObj['singer'] = singer[i].attrs['title']
        resultArr.append(tempObj)

    driver.close()
    return resultArr
