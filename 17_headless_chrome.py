import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument = ('window-size = 2560x1600')

browser = webdriver.Chrome('/Users/thwnsdyd/Desktop/공부/Python/web_scrapping/chromedriver', options = options)
browser.maximize_window()

# 페이지이동
url = 'https://play.google.com/store/movies/top'
browser.get(url)


browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 가장아래까지 내리기
import time 
interval = 2 # 2초에 한번씩 내림

# 현재 문서높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')


# 반복수행
while True:
    # 화면 가장 아래로 스크롤 내리기
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
    # 페이지 로딩대기
    time.sleep(interval)

    # 현재 문서높이를 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height:
        break
    
    prev_height = curr_height
print('스크롤 완료')
browser.get_screenshot_as_file('google_movie.png')
# 현재 할인중인 영화만 정보를 스크래핑 하는 코드
# 동적 페이지를 스크래핑 할때의 방법

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all('div', attrs  = {'class' : ['ImZGtf mpg5gc',"Vpfmgd"]})
# attrs 안에서 리스트 사용가능
# 이런식으로 attrs로 찾을 경우 두번씩 출력되는 경우가있다
movies = soup.find_all('div', attrs  = {'class' : "Vpfmgd"})
# with open('movie.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
#     # html 문서를 예쁘게 출력
#     # 저장된 html 을 보면 우리가 본화면과 다르다 user agent 때문에

for movie in movies:
    title = movie.find('div', attrs = {'class' : 'WsMG1c nnK0zc'}).get_text()
    
    # 할인전 가격
    original_price = movie.find('span', attrs = {'class' : 'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "할인되지않은 영화 제외")
        continue

    # 할인된가격
    price = movie.find('span' , attrs = {'class' : 'VfPpfd ZdBevf i5DZme'}).get_text()

    # 링크
    link = movie.find('a', attrs = {'class' : 'JC71ub'})['href']
    # 올바른 링크 :  https://play.google.com/ + link    
    link = 'https://play.google.com' + link
    
    print(f'제목 : {title}')
    print(f'할인 전 금액 : {original_price}')
    print(f'할인 후 금액 : {price}')
    print(f'링크 : {link}')
    print('------------------------------------------------------------------------------------')
browser.quit()