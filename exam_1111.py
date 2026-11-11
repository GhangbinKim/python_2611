import math
import random


''' print(math.sqrt(16))
print(math.pow(2,1))
 '''
# 난수 모듈
# 무작위 값 생성
# 테스트에 사용
''' print(random.randint(-100, 100)) '''

# 직접 모듈 생성해보기
# import ex1 : 모든 걸 다 불러오기
# from ex1 import funA : 선택한 것만 불러오기
''' import ex1
from ex1 import funA
print(ex1.funA())
print(ex1.funB())
print(ex1.funC()) '''

# 날짜/시간 모듈
# 현재 시간 확인, 날짜 계산 사용
''' import datetime
print(datetime.datetime.now()) '''

# 시간 제어 모듈
# 시간 흐름을 제어하는 모듈
# 프로그램을 잠시 멈출 때 사용
''' import time
time.sleep(3) # 프로그램을 3초동안 멈춤
print("3초 후 실행") # 3초 후 실행 '''

# 시스템 모듈
# 파이썬 실행 환경을 다루는 모듈
''' import sys
print(sys.version) '''

# 운영체제 모듈
# 운영체제(OS)와 관련된 기능 제공
# 파일/폴더 경로 처리에 사용
''' import os
print(os.getcwd()) '''

# 데이터 형식 모듈
# JSON형식으로 데이터를 변환
# JSON : 데이터를 약속된 모양으로 적는 방식
# Web, API 저장에 사용함.
# API : 프로그램끼리 대화하는 방법(규칙)
''' import json
data={
    'name' : 'jin',
    'age' : 22
}
print(json.dumps(data)) '''

# 정규표현식 모듈
# 문자열 패턴 검사 모듈
# 형식 확인(아이디, 이메일)에 사용
''' import re
# 문자열이 'hi'로 시작하는지 확인
print(bool(re.match('hi', 'hi python'))) '''

# csv 파일 모듈
# csv(엑셀) 파일을 읽고 쓰는 모듈
# 데이터 저장 / 분석 기초에 사용
''' import csv
with open('test.csv', 'w', newline='') as f:
    csv.writer(f).writerow(['name', 'score']) '''

# 자료구조 모듈
# 자료구조를 편하게 쓰도록 도와주는 것
# 카운트, 큐, 딕셔너리 확장 기능 제공

from collections import Counter

# 문자열에서 각 글자의 개수를 count 한다.
print(Counter('banana'))