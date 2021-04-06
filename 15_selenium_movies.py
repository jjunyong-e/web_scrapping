# 현재 할인중인 영화만 정보를 스크래핑 하는 코드
# 동적 페이지를 스크래핑 할때의 방법

import requests
import re
from bs4 import BeautifulSoup
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept-Language' : 'ko-kr'
    # 한국어 사이트를 받아온다
    }
url = 'https://play.google.com/store/movies/top'
res = requests.get(url,headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


movies = soup.find_all('div', attrs  = {'class' : "ImZGtf mpg5gc"})


# with open('movie.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
#     # html 문서를 예쁘게 출력
#     # 저장된 html 을 보면 우리가 본화면과 다르다 user agent 때문에

for movie in movies:
    print(movie.find('div', attrs = {'class' : 'WsMG1c nnK0zc'}).get_text())
    