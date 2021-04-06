import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument = ('window-size = 2560x1600')
options.add_argument = ('user-agent= Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')

browser = webdriver.Chrome('/Users/thwnsdyd/Desktop/공부/Python/web_scrapping/chromedriver', options = options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

de_val = browser.find_element_by_id('detected_value')
print(de_val) 
browser.quit()

# Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/
# 537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
# 원래 유저에이전트

# <selenium.webdriver.remote.webelement.WebElement (session="1aa95f07479c3ae16102b9950f5a0f93",
#  element="971a182b-b1f4-4744-82f5-b36715d90115")>
# 헤드리스 크롬사용시 유저에이전트