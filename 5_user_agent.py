import requests

url = 'http://instagram.com/'
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print('웹스크래핑 진행합니다')

with open('isntagram_with_user_agent.html', 'w', encoding = 'utf8') as f:
    f.write(res.text)

