import requests

res = requests.get("http://google.com")
res.raise_for_status()
#print("응답코드 : " ,res.status_code)
# 200 이면 정상

#res = requests.get("http://yahoo.com")
#print("응답코드 : " ,res_2.status_code)


#if res.status_code == requests.codes.ok:
#    print('정상입니다')
#else:
#    print('문제가 생겼습니다. [에러코드' , res_1.status_code, ']')
#res.raise_for_status()
# 문제가 생겼을 때는 이줄에서 끝난다 
print('웹스크래핑 진행합니다')
# 이것이 출력된것은 윗줄에서 문제가 없었기때문이다

print(len(res.text))
print(res.text)

with open('mygoogle.html', 'w', encoding = 'utf8') as f:
    f.write(res.text)