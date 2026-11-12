import numpy as np

''' 
# 만약 설치가 안될 시...
import sys # 파이썬이 설치된 경로 추출 위한 라이브러리

print(sys.executable) # 경로 추출
# 터미널 : 추출한 경로 -m pip install 외부라이브러리이름
'''
''' 
Numpy : Python에서 수학, 데이터 분석을 쉽게 할 수 있도록 도와주는 라이브러리
ndArray : 숫자를 여러차원으로 저장할 수 있는 배열
Numpy로 가능한 것들
 - 숫자 묶음 생성
 - 평균, 합계, 최댓값
 - 배열
 - 2차원 표(행렬)
'''

''' print('===== 일반 리스트 =====')
a=[1,2,3]
b=[4,5,6]
print(a+b) '''

''' print('===== numpy 01 =====')
a = np.array([1,2,3])
b = np.array([4,5,6])
# np.array([]) : 리스트처럼 보이지만 실제로는 수학용 배열이다. 모든 원소가 같은 타입
print(a+b) '''

''' print('===== numpy 02 =====')
arr1 = np.array([1,2,3,4])
arr2 = [1,2,3,4]
print(type(arr1))   # numpy로 이루어진 다차원 배열
print(type(arr2))   # python 리스트 형태 '''

''' print('===== numpy 03 =====')
# 1차원 배열 : 숫자가 한 줄로 늘어선 형태
# 2차원 배열 : 숫자가 가로와 세로로 된 표 모양
# 3차원 배열 : 2차원 배열이 여러 장 겹친 입체 모양

## 2차원 ndArray 생성
# 1차원 배열 2개가 리스트로 묶인 형태
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr3 = np.array([[[1,2,3,4],[1,2,3,4]],
                [[1,2,3,4],[1,2,3,4]]])

print(arr2) #2차원 배열
print(arr3) #3차원 배열 '''

''' print('===== numpy 04 =====')
a = np.array([1,2,3,4])
print(a+1)
print(a*2)
print(a**2) # for문을 쓰지 않고도 계산이 가능하다! '''

''' 
print('===== numpy 05 =====')
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3,4], [5,6,7,8]])
arr3 = np.array([[[-0.1, 0.2, 0.3, 0.4], [5,6,7,8]], [[1,2,3,4],[1,2,3,4]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# shape : 배열의 형태(배열의 구조를 튜플로 보여줌)
# 튜플 : 리스트와 비슷하지만 가장 큰 차이점은 한 번 생성한 튜플의 
print(arr1.shape)   # (4, ) - 4
print(arr2.shape)   # (2,4) = 8
print(arr3.shape)   # (2,2,4) = 16

# size : 배열 요소의 총 개수
print(arr1.size)    # 4
print(arr2.size)    # 8
print(arr3.size)    # 16

# dtype : 배열 요소의 데이터 타입
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

# itemsize : 배열 원소 하나가 차지하는 메모리의 크기
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# data : 배열의 실제 데이터가 저장된 메모리 버퍼
print(arr1.data)
print(arr2.data)
print(arr3.data) 
'''
''' 
print('===== numpy 06 =====')
# ndArray T : 전치 행렬(행/열을 서로 바꾸는 것)
arr = np.array([[1,2,3],[4,5,6]])
print("원래 배열")
print(arr)

print("전치 배열")
print(arr.T)
'''
''' 
print('===== numpy 07 =====')
#ndArray.flatten() : 1차원으로 펼치기
arr = np.array([[1,2,3],[4,5,6]])
print("원래 배열")
print(arr)

print("1차원으로 펼친 배열")
print(arr.flatten())

flat = arr.flatten()
flat[0] = 100

print('배열 출력')
print(flat)
 '''
''' 
print('===== numpy 08 =====')
# ndArray.reshape() : 배열 모양 바꾸기
arr = np.array([1,2,3,4,5,6])

print("원래 배열")
print(arr)

# reshape 할 때 원본과 size가 같아야 함
arr2 = arr.reshape(2, 3)
print('reshape 배열')
print(arr2)
 '''
''' 
print('===== numpy 09 =====')
# ndArray.sum() : 합계 구하기
# axis : 어느 축을 기준으로 계산할 것인가
# axis 옵션
# axis=0 : 열 방향 합
# axis=1 : 행 방향 합
arr = np.array([[1,2,3],
                [4,5,6]])
print("전체 합 :", arr.sum())
print("열 방향 합(axis=0) :", arr.sum(axis=0))
print("행 방향 합(axis=1) :", arr.sum(axis=1))
 '''
''' 
print('===== numpy 10 =====')
# ndArray.mean() : 평균 구하기
# axis : 어느 축을 기준으로 계산할 것인가
# axis 옵션
arr = np.array([[1,2,3],
                [4,5,6]])
print("전체 평균 :", arr.mean())
print("열 방향 평균(axis=0) :", arr.mean(axis=0))
print("행 방향 평균(axis=1) :", arr.mean(axis=1))
 '''
''' 
print('===== numpy 11 =====')
# ndArray.min() : 최솟값 구하기
# ndArray.max() : 최댓값 구하기
# axis : 어느 축을 기준으로 계산할 것인가
# axis 옵션
# axis=0 : 열 방향 합
# axis=1 : 행 방향 합
arr = np.array([[1,2,3],
                [4,5,6]])
print("전체 최솟값 :", arr.min())
print("전체 최댓값 :", arr.max())

print("열 방향 최솟값(axis=0) :", arr.min(axis=0))
print("행 방향 최댓값(axis=1) :", arr.min(axis=1))

print("열 방향 최솟값(axis=0) :", arr.max(axis=0))
print("행 방향 최댓값(axis=1) :", arr.max(axis=1))
 '''

''' print('===== numpy 12 =====')

zero = np.zeros((3,4))
print(zero)
 '''
''' 
print('===== numpy 13 =====')
one = np.ones((2,3,4))
print(one)
'''
''' 
print('===== numpy 14 =====')
full = np.full((4,4), 3)
print(full)
 '''
''' 
print('===== numpy 15 =====')

arr2 = np.array([[1,2,3,4], 
                [5,6,7,8]])

print(np.zeros_like(arr2))
print(np.ones_like(arr2))
print(np.full_like(arr2, 2))
'''
''' 
print('===== numpy 16 =====')

rand = np.random.randint(-100, 100, (2, 3))
# -100 이상 100 미만의 정수 중에서
# 2행 3열의 배열 생성
print(rand)

np.random.seed(1) # 난수 생성 기준을 1로 고정
print(np.random.randint(0, 10, (2,3)))

np.random.seed(2) # 난수 생성 기준을 2로 고정
print(np.random.randint(0, 10, (2,3)))
 '''

print('===== numpy 17 =====')
arr1 = np.array([1,2,3,4])      # 1차원 배열, shape=(4, )
arr2 = np.array([[1,2,3,4],     # 2차원 배열, shape=(2,4)
                [5,6,7,8]])

# 1차원 배열 인덱싱
print('파이썬 기본 리스트 예시')
li = [1,2,3,4]
print(li[0])

print('1차원 배열 인덱싱')
print(arr1[0])

# 2차원 배열 인덱싱
print('2차원 배열 인덱싱')
print(arr2[0, 1])   # 첫 번째 행, 두 번째 열
print(arr2[1, 2])   # 두 번째 행, 세 번째 열

# 2차원 배열 슬라이싱
print(arr2[1:2, 1:3])   # 행 : 1 이상 2 미만, 열 : 1 이상 3 미만


# Fancy 인덱싱 : 인덱스 번호를 리스트/배열로 여러 개 전달
print('1차원 배열 fancy 인덱싱')
print(arr1[[0,1,3]])



print('2차원 배열 fancy 인덱싱')
print(arr2[[0,1], [1,3]])
