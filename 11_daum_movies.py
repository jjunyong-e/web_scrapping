# 각 연도별 관객순위가 높은 영화 이미지를 5개씩 다운하는 실습
import requests
import re
from bs4 import BeautifulSoup
# https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR
# https://search.daum.net/search?w=tot&q=2018%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR
# q부분이 년도의 정보를 담고있다

# 2019 년부터 2011년까지의 url 을 반복
for i in range(2015,2020):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all('img', attrs= {'class' : 'thumb_img'})
    for idx, image in enumerate(images):
        
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:'+ image_url
            
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open('{}년movie{}.jpg'.format(i,idx+1),'wb') as f:
            f.write(image_res.content)
        if idx >= 4:
            break
        # 상위 다섯개만 다운