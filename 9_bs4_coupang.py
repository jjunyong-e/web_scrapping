import requests
from bs4 import BeautifulSoup
import re

# 내일까지 노트북을 사야한다
# 로켓배송에 광고가 아닌것이 중요하다
# https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor=
# page 부분만 조절을 하면될것같은데
# 이방식은 http method 의 get 방식이다
# 보안 내용은 post 방식을 이용한다 큰 용량의 경우도 post방식을 이용한다


url ='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor='
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all('li', attrs = {'class': re.compile('^search-product')})
for item in items:
    # 추가 할인 쿠폰있는것만
    badge_benefit = item.find('span',attrs = {'class':'badge badge-benefit'})
    if badge_benefit is None:
        continue # 쿠폰없는것은 제외

    name = item.find('div',attrs = {'class':'name'}).get_text()# 이름
    # 애플제품제외
    if 'Apple' in name:
        print('애플 제품은 안써요')
        continue

    price = item.find('strong',attrs = {'class':'price-value'}).get_text() # 가격

    # 리뷰 100 개이상 평점 4.5 이상만 조회
    rating = item.find('em', attrs = {'class':'rating'}) # 평점
    rating_num = item.find('span', attrs = {'class':'rating-total-count'}) # 리뷰수

    if rating:
       rating = rating.get_text()
       
    else:
        rating = '평점없음'
        print('평점없는 상품 제외합니다')
        continue

    if rating_num:
        rating_num = rating_num.get_text()
        rating_num = rating_num[1:-1]
    else:
        rating_num = '리뷰없음'
        print('리뷰없는 상품 제외합니다')
        continue
    
    if float(rating)  >= 4.5 and float(rating_num) >=100:
        
        print(name, price, rating, rating_num)