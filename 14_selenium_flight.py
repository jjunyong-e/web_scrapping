from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/Users/thwnsdyd/Desktop/공부/Python/web_scrapping/chromedriver')

browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url)

# 가는날선택 클릭
browser.find_element_by_link_text('가는날 선택').click()

# 가는 날짜 클릭 이번달 22일

browser.find_elements_by_link_text('22')[0].click()

# 오는 날짜 클릭 다음달 22일 

browser.find_elements_by_link_text('22')[-1].click()

# 도착지 클릭

browser.find_element_by_link_text('도착지로 설정(홍콩)').click()

# 항공권 검색 버튼 클릭

browser.find_element_by_link_text('항공권 검색').click()

try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div[1]/div[7]/ul/li[1]')))
    # 최대 10초 기다리고 아니면 브라우저 종료
    # 성공했을때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit() 



