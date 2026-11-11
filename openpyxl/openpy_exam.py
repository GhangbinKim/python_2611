'''
# 설치가 안될 시
import sys
# 파이썬이 설치된 경로 추출
print(sys.executable)
# 터미널 : 추출한 경로 -m pip install 외부라이브러리이름
''' 



# openpyxl 불러오기 / 모든 기능을 불러옴
import openpyxl
# from openpyxl import *

# 버전 확인
print(openpyxl.__version__)

''' 
# ==엑셀 파일 생성, 기본 시트 선택 == #
# 새로운 엑셀 파일 만들기
# 새 엑셀 파일을 만들겠다 라는 의미
w1 = Workbook()

# 만들어진 엑셀 파일에서 기본 시트를 선택
ws = w1. active

#지금 만든 엑셀 파일을 실제 파일로 저장 #
w1. save('test.xlsx')
 '''