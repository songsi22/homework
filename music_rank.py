import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

for i in soup.select('#body-content > div.newest-list > div > table > tbody > tr'):
    rank = soup.select_one(
        '#body-content > div.newest-list > div > table > tbody > tr')
    rank = i.select_one('td.number').text
    rank = str(rank).strip()[0:2].rstrip('\n')
    title = soup.select_one(
        '#body-content > div.newest-list > div > table > tbody > tr')
    title = i.select_one(' td.info > a.title.ellipsis').text
    title = str(title).strip()
    singer = soup.select_one(
        '#body-content > div.newest-list > div > table > tbody > tr')
    singer = i.select_one('td.info > a.artist.ellipsis').text

    print(rank, title, singer)
