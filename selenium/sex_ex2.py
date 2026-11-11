# 요소 찾는 방법은 3가지가 있음.
# 1. 태그 이름(TAG_NAME)
# 2. 침ㄴ


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

# 태그 이름

div_elements = driver.find_elements(By.TAG_NAME, 'div')
print('TAG_NAME으로 찾은 div 태그 개수 : ', len(div_elements))

# class로 요소 찾기(CLASS_NAME)
# - html에서 class='text'처럼 지정된 class 이름으로 요소 찾기
# - Selenium에서 가장 자주 사용하는 방식 중 하나
# - class에 공백이 포함된 경우 CLASS_NAME으로 바로 찾기 어려움

first_quote_text = driver.find_element(By.CLASS_NAME, 'text')
print('\n CLASS_NAME으로 찾은 첫 번째 명언 : ', first_quote_text.text)

## id로 요소 찾기
# - id는 보통 페이지에서 '유일'하게 존재
# - 정확하게 찾고 싶을 때 가장 안정
element = driver.find_element(By.ID, "username")
print('\nID로 찾은 요소의 태그 이름 : ', element.tag_name)

# find element vs find_elements
# - find_element : 요소 1개만 찾음(없으면 에러 발생)
# - find_elements : 요소 여러 개를 찾고 리스트로 반환(없으면 빈 리스트)

one_quote_block = driver.find_element(By.CLASS_NAME, 'quote')
many_quote_block = driver.find_elements(By.CLASS_NAME, 'quote')

print('\nfind_element로 찾은 quote 블록 1개 : ', type(one_quote_block))
print('\nfind_elements로 찾은 quote 블록 개수 : ', len(many_quote_block))


## xPath
# - xPath는 HTML의 구조를 이용해 요소를 찾는 방법
# - id나 class로 찾기 어려울 때 사용

# XPath로 첫 번째 명언 검색
xpath_quote_text = driver.find_element(
    By.XPATH,
    "//div[@class='quote']/span[@class='text']"
)

'''
 - // : 문서 전체에서 검색
  - div[@class='quote'] : div 태그 중 class='quote'인 요소
  - / : 바로 아래 자식(child) 관계
  - span[@class='text'] : 위에서 찾은 div 바로 아래에 있는 span 중에서 class='text'인

의미
 - class='quote'인 div 자식 중에서 class='text'인 span을 찾아라
'''

print('\nxPath로 찾은 첫번째 명언 :', xpath_quote_text.text)

#XPath의 위치 인덱스는 1부터 시작
xpath_first_block = driver.find_element(
    By.XPATH,
    "(//div[@class='quote'])[1]"
)

# 첫 번째 블록 내부에서 작성자 검색
xpath_first_author = xpath_first_block.find_element(
    By.CLASS_NAME,
    'author'
)

print('xpath로 찾은 첫 번째 저자 : ', xpath_first_author.text)

driver.quit()