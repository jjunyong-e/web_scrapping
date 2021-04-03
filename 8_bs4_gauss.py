import requests
from bs4 import BeautifulSoup
import numpy as np
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=675554'
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
# gauss_titles = soup.find_all('a', attrs= {'class' : 'title'})
# for title in gauss_titles:
    # print(title.get_text())
# 이방식은되지않는다 왜냐하면 'td'엘리먼트이다

# gauss_titles = soup.find_all('td', attrs= {'class' : 'title'})
# title = gauss_titles[0].a.get_text()

# td 밑에있는 a 에 접근하자

# 사이트내의 모든 제목가져오기
# for title in gauss_titles:
    # print(title.a.get_text())
    # print('링크 : ', "https://comic.naver.com"+title.a['href'])
    # print()

gauss_ratings = soup.find_all('div', attrs= {'class' : 'rating_type'})
# 사이트내의 모든 평점가져오기
rating_lst = []
for rating in gauss_ratings:
    rating_lst.append(rating.strong.get_text())

print(rating_lst)
    