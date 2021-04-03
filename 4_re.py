# regular expression - 정규식

# 주민등록번호
# 960419 - 111111 - 올바른것
# abcdef - 1111111 - 올바르지않은것

import re
# abcd, book, desk
# 여기에서 한글자가 기억이 안나서 ca@e 
# care cafe case cave - 이것들을 조사를 해야한다

p = re.compile("ca.e")
# 패턴
# print(m.group())

# 매치되지않았다면 에러가발생
# AttributeError: 'NoneType' object has no attribute 'group'
# m2 = p.match("face")
# print(m2.group())

def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print('m.start() : ' , m.start()) # 일치하는 문자열의 시작 index
        print('m.end() : ' , m.end()) # 일치하는 문자열의 끝 index 
        print('m.span() : ' , m.span()) # 일치하는 문자열의 시작 / 끝 index
        
    else:
        print('매칭되지않음')


# m = p.match('careless')
# print_match(m)
# match : 주어진 물자열의 처음부터 일치하는지 확인한다
# 따라서 careless 역시 만족을 한다 

# m = p.search('good care')
# search : 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)
# m.group() :  care
# m.string :  good care
# m.start() :  5
# m.end() :  9
# m.span() :  (5, 9)

# lst = p.findall('careless ,good care, cafe') # findall : 일치하는 모든것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile('원하는 형태')
# 2. p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 3. p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열' ) : 일치하는 모든것을 리스트 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) --> 하나의 문자를 의미한다 > care , cafe , case (o) | caffe (x)
# ^ (^de) --> 문자열의 시작 > desk, destination (o) | fade(x)
# $ (se$) --> 문자열의 끝 > case, base (o) | face (x) 
# 이외 다른것들이 많지만 이것만 먼저 배우기
