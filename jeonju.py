import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?query=%EC%A0%84%EC%A3%BC%EC%97%AC%ED%96%89&nso=&where=blog&sm=tab_viw.all"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

title_lst = []

title1 = soup.find_all('a', attrs= {'class' : 'api_txt_lines total_tit'})

# for _ in title1:
    # print(_.get_text())
for _ in title1:
    print(_.get_text())