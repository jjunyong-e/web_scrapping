import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# 텍스트만 가져온것
# print(soup.a)  soup 객체에서 첫번째로 발견된 a엘리먼트 정보 가져옴
# print(soup.a.attrs)  a 엘리먼트의 속성을 가져온것
# print(soup.a['href'])  a 엘리먼트의 'href' 속성값을 가져온것


# <a href="/mypage/myActivity.nhn" class="Nbtn_upload" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# print(soup.find('a', attrs = {'class' : 'Nbtn_upload'})) # class = 'Nbtn_uplaod'인 a엘리먼트를 찾아줘
# print(soup.find(attrs = {'class' : 'Nbtn_upload'})) # class = 'Nbtn_upload'인 엘리먼트를 찾아줘

for _ in range(1,11):
    if _ < 10:
        print(soup.find(attrs = {'class' : 'rank0'+str(_)}).a['title'])
    else:
        print(soup.find(attrs = {'class' : 'rank'+str(_)}).a['title'])

# 실습을 이용한 1 위부터 10위까지 a 엘리먼트중 타이틀 부분만 출력 
# 여기까지는 안배웠는데 내가생각해도 잘한듯 ^__^

