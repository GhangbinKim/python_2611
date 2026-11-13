import numpy as np

''' arr = np.array([[3, 6, 9],
                [2, 4, 8],
                [5, 7, 1]])


## 1. Numpy 심화문제1
# 문제
# 1. arr의 shape과 ndim을 출력하시오.
print(arr.shape)
print(arr.ndim)

# 2. 열 방향 평균을 구하시오.
print(arr.mean(axis=0).round(1))

# 3. 행 방향 최댓값을 구하시오.
print(arr.max(axis=1))
# 4. arr을 전치행렬로 만든 후 shape을 출력하시오.
Trans = arr.T
print(Trans)
print(Trans.shape)
# 5. arr을 1차원으로 펼친 뒤 최솟값을 구하시오.
one_dim = arr.reshape(-1)
print(one_dim)
print(one_dim.shape)
print(one_dim.min())
# 6. arr을 (1, 9) 형태로 reshape 하시오.
one_dim_re = one_dim.reshape(1,9)
print(one_dim_re) '''

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])
''' 
## 2. Numpy 심화문제2
# 문제
# 1. arr의 dtype과 itemsize를 출력하시오.
print(arr.dtype)
print(arr.itemsize)
# 2. axis=0 기준 합을 구하시오.
print(arr.sum(axis=0))
# 3. axis=1 기준 평균을 구하시오.
print(arr.mean(axis=1))
# 4. arr을 (4,2) 형태로 reshape 하시오.
re = arr.reshape(4,2)
print(re)
# 5. reshape한 배열을 전치한 결과의 shape을 구하시오.
Trans = re.T
print(Trans)
print(Trans.shape)
# 6. arr.flatten()으로 만든 배열의 shape은 무엇인가?
flat = arr.flatten()
print(flat.shape) '''

'''
    1. 불리언 인덱싱(Boolean Indexing)
    - 조건에 맞는 데이터만 추출
    - True에 해당하는 데이터만 선택하여 새로운 배열 생성
'''

print('== 1. 불리언 인덱싱(Boolean Indexing) ==')
arr = np.array([10, 20, 30, 40, 50])
# 조건식 확인
print(arr>25)

# 25보다 큰 값만 출력
#print(arr[arr>25])

# 2차원 배열에서도 사용 가능
arr2 = np.array([[10,20,30],
                 [40,50,60]])

print(arr2[arr2>=40])



'''
    2. np.where()
    조건에 따라 서로 다른 값을 선택하는 함수
    np.where(조건, 참일 때 값, 거짓일 때 값)
'''

print('== 2. np.where() ==')
result = np.where(arr>=30,1,0)
print(result)

scores = np.array([80, 20, 66, 78, 54])
result = np.where(scores >= 60, '합격', '불합격')
print(result)

# 조건에 해당되는 위치 찾기
result = np.where(arr>=30)
print(result[0])

'''
    3. np.count_nonzero()
    배열에서 0이 아닌 원소의 개수를 구하는 함수
    조건식과 사용하면 조건을 만족하는 데이터의 개수 계산
    True는 개수를 셀 때 1, False는 0으로 취급
'''
print('== 3. np.count_nonzero() ==')

# 0이 아닌 데이터 개수
arr = np.array([0, 10, 0, 20, 0, 30])
print(np.count_nonzero(arr))

# 30 초과인 데이터 개수
arr = np.array([10,20,30,40,50])
print(np.count_nonzero(arr>30))

# 짝수의 개수
arr = np.array([1,2,3,4,5,6])
print(np.count_nonzero(arr%2==0))



'''
  4. np.argmax()
  배열에서 최대값이 있는 위치(인덱스)를 반환
  최댓값이 여러 개면 첫 번째 위치 반환
  max() 최댓값, argmax() 최댓값의 인덱스
'''
print('== 4. np.argmax() ==')

arr = np.array([10,40,60,80,20])
print(arr.max())
print(arr.argmax())


arr2 = np.array([[10,30,70],
               [90,20,50]])
print(arr2.argmax())

# 열별 최댓값의 행 인덱스
print(arr2.argmax(axis=0))

# 행별 최댓값의 열 인덱스
print(arr2.argmax(axis=1))

'''
  5. np.unravel_index()
  1차원 인덱스를 다차원 배열의 좌표로 변환하는 함수
  2차원 배열에서 최댓값이 몇 행, 몇 열인지 확인할 때 사용
  np.unravel_index(인덱스, 배열의 shape)
'''
print('== 5. np.unravel_index() ==')
arr = np.array([[10,20,30],
                [40,50,60]])

# 최댓값의 인덱스 확인
index = arr.argmax()
print(index)

# 1차원 인덱스를 2차원 좌표로 변환
position = np.unravel_index(index, arr.shape)
print(position)
print(arr[position]) # arr[5]는 오류가 뜬다!

'''
  6. np.clip()
    배열의 값을 지정한 최소, 최대 범위로 제한하는 함수
    최솟값보다 작으면 최솟값으로 변경
    최댓값보다 크면 최댓값으로 변경
    범위 안의 값은 그대로 유지
    np.clip(배열, 최솟값, 최댓값)
'''
print('== 6. np.clip() ==')

# 최소 20, 최대 100으로 제한
arr = np.array([10,40,50,90,130])
result = np.clip(arr, 20, 100)
print(result)

# 점수가 100점을 초과하지 않도록 설정
scores = np.array([70, 90, 110, 135])
result = np.clip(scores, 0, 100)

print(result)


'''
  7. 브로드캐스팅(Broadcasting)
    서로 다른 형태의 배열끼리 연산할 수 있도록 하는 기능
    배열의 크기가 달라도 일정한 조건을 만족하면 연산 가능
    작은 배열을 큰 배열에 맞춰 연산하는 방식
    실제로 배열을 복사해서 늘릴 필요는 없다!
'''
print('== 7. 브로드캐스팅 ==')

arr = np.array([10,20,30])
print(arr+5)

# 2차원 배열과 1차원 배열 연산
arr1 = np.array([1,2,3])

arr2 = np.array([[10,20,30],
                [40,50,60]])

print(arr1+arr2)

# arr1의 shape : (3, )
# arr2의 shape : (2, 3)




















