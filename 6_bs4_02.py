import requests
from bs4 import BeautifulSoup
import lxml
url = "https://comic.naver.com/webtoon/weekday.nhn"

res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")
rank01 = soup.find('li', attrs = {'class' : 'rank01'})

#print(rank01.a.get_text())
# 01 파일에 있던것보다훨씬 편한 get_text()이런!~
# print(rank01.next_sibling) 이코드실행시 공백만 출력된다 > 시블링 사이에 개행 관계때문
# rank02 = rank01.next_sibling.next_sibling
# rank03 = rank02.next_sibling.next_sibling
# print(rank03.a.get_text()) # 3위의 텍스트가 출력

# rank02 = rank03.previous_sibling.previous_sibling
# print(rank02.a.get_text()) 
# print(rank01.parent)

# rank02 = rank01.find_next_sibling('li') # 위에서처럼 개행이있는경우인지 없는경우인지 모를경우에는 find_next_sibling('태그')를 이용한다
# print(rank02.a.get_text())
# rank03 = rank02.find_next_sibling('li')
# print(rank03.a.get_text())
# rank02 = rank03.find_previous_sibling('li')
# print(rank01.find_next_siblings('li')) # 다음의 모든 시블링들 가져옴


# <a
# onclick="nclk_v2(event,'rnk*p.cont','597447','1')"
# href="/webtoon/detail.nhn?titleId=597447&amp;no=384" 
# title="프리드로우-제381화 불법 사이트 (1)">
# 프리드로우-제381화 불법 사이트 (1)  : 태그가 닫히고 있는 부분 -- > 텍스트
# </a>
webtoon = soup.find('a', text= "프리드로우-제381화 불법 사이트 (1)")
print(webtoon)