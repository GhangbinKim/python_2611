### 정규 표현식
# 문자열에서 특정한 규칙이나 패턴을 가진 데이터를 추출, 검색, 치환하기 위한 표현 방식
# - 문자열 검색
# - 데이터 추출
# - 문자열 치환
# - 입력값 검사

import re
''' 
## 정규 표현식 
text = '내 혈압은 120mmHg 입니다.'
print('120' in text)

pattern = r'\d+'    # \d+ : 숫자가 1개 이상인 패턴을 찾아라

result = re.findall(pattern, text)

print(result) '''

''' 
## 정규표현식 : 기본패턴
sample = 'abc123xyz456'

# 숫자찾기
print(re.findall(r'\d+', sample))

# 문자찾기 # + : 1개 이상 / * : 0개 이상 / ? : 0개 또는 1개 
print(re.findall(r'[a-z]', sample))
print(re.findall(r'[a-z]+', sample))
 '''
''' 
## 정규표현식 : 특정형식 찾기

data='이메일은 test123@gmail.com 입니다.'
# 이메일 형식 간단히 찾기
email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, data)
print(emails)
# \w : 문자 또는 숫자
# @ : @문자
# \. : .은 정규식에서 특수 문자이기 때문에 \를 붙여야 함.

## 정규표현식 : re 모듈 주요 함수
# re.findall
# re.search()
# re.match()
# re.fullmatch()
# re.sub()

text = 'python 123 java 456'
result = re.search(r'\d+', text)
print(result.group())
 '''
## 정규표현식 : 문자열 치환
text2 = '가격은 12000원 입니다.'

# 숫자 제거
new_text = re.sub(r'\d+', '', text2)
print(new_text)

## 정규식 vs 일반 문자열 처리 비교
text3 = '몸무게: 70kg, 키: 170cm'

# 단순 split 사용
print(text3.split(','))

# 정규식으로 숫자만 추출
nums = re.findall(r'\d+', text3)
print(nums)