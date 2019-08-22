import requests
from bs4 import BeautifulSoup
import pandas as pd


def crawling(url):
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles = [content.get_text() for content in soup.select('.play_txt_01')]
    artists = [content.get_text() for content in soup.select('.play_txt_02')]
    title_artist_list = list(zip(titles, artists))
    return title_artist_list


def make_url(param):
    base_url = "http://www.ziller.co.kr/SingingroomSearchList.do"
    query = "?currpage=" + str(param)
    url = base_url + query
    return url


i = 1
while(1):
    url = make_url(i)
    title_artist_list = crawling(url)
    if not title_artist_list:
        break
    data = pd.DataFrame(title_artist_list)
    print(data)
    data.to_csv('C:\claion\Singlist-data\song_list.csv', header=None,
                mode='a',  index=False, encoding='utf-8')
    i = i + 1
