
###### 소수 함수 나의 버전
''' def is_prime_num(num):
    for i in range(2, num):
        if num%i==0:
            return False
    #print("True")
    return True

prime=is_prime_num(17)
print(prime) '''

##### 소수함수 선생님 버전
''' def get_divisors_sum(num):
  s = 0
  i = 1
  while i <= num:
    if num % i == 0:
      s += i
    i += 1
  return s

def is_prime_number_v2(num):
  return get_divisors_sum(num) == num + 1

num=21
print(get_divisors_sum(num))
print(is_prime_number_v2(num)) '''


### 01. 리스트 및 반복문 제어
# 문제 1. 리스트에 순서대로 2, 1, 5, 6, 7을 한 번에 담아주세요.
''' a=[2,1,5,6,7]
print(a) '''

#문제 2. 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7을 하나씩 담아주세요.
''' a=[]
a.append(2)
a.append(1)
a.append(5)
a.append(6)
a.append(7)
print(a) '''

# 문제 3. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. 그리고 '+=' 연산자를 이용해서 '토', '일'을 한 번에 추가해주세요.
''' day=['월', '화', '수', '목', '금']
print(day)
day.append('토')
day.append('일')
print(day) '''

# 문제 4. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. 그리고 가장 마지막 요소를 출력해주세요.
''' day=['월', '화', '수', '목', '금']
#print(len(day)-1)
print(day[len(day)-1]) '''

# 문제 5. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. 그리고 while문을 이용해서 요소 전부 출력해주세요.
''' day=['월', '화', '수', '목', '금']
i=0
while i<len(day):
    print(day[i])
    i+=1 '''

# 문제 6. 리스트에 순서대로 2, 1, '오', 6, 7을 한 번에 담아주세요. 그리고 리스트 안에 있는 '오'를 정수 5로 변경해주세요.
''' a=[2, 1, '오', 6, 7]
print(a)
a[a.index('오')]=5 
print(a) '''

# 문제 7. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. '화'가 리스트 안에 들어있는지 알려주세요.
''' day=['월', '화', '수', '목', '금']
def day_in(day):
  if '화' in day:
    return True
  else:
    return False
print(day_in(day)) '''

# 문제 8. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. '화'가 리스트 안에서 몇 번째 데이터인지 알려주세요.
''' day=['월', '화', '수', '목', '금', '화']

def num_day(day):
  num=[]
  for i in range(0, len(day)):
    if day[i]=='화':
      num.append(i)
      
    #return num
  print(num)

print(num_day(day)) '''

# 문제 9. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. 리스트에 있는 '금'을 삭제하는 3가지 방법을 보여주세요.
''' day=['월', '화', '수', '목', '금', '화']
day.remove('금')
del a[4]
del a[-1]
del a[a.index('금')]
 '''

### continue / break
''' for dan in range(1, 10):
    if dan==4:
        continue
    if dan==8:
        break
    print(f"{dan}단") '''

### dictionary
''' ages = {
    "THOMSON" : 37,
    "CURRY" : 40,
    "Lebron" : 41,
    "Durant" : 39
}
print(ages) '''

#문제 1. 딕셔너리에 각 달의 마지막 날들을 한 번에 담기
''' month={
    "1월" : 31,
    "2월" : 28,
    "3월" : 31
} '''

# 문제 2. 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기
#ver.1
''' last_days_m={}
for i in range(1, 13):
    month=str(i)+"월"
    end_day=30
    if i==2:
        end_day=28
    elif i in (1,3,5,7,8,10,12):
        end_day=31
    last_days_m[month]=end_day
print(last_days_m) '''


#ver.2
''' end_days=[31,28,31,30,31,30,31,31,30,31,30,31]
month_end={}
for i, end in enumerate(end_days):
    month = str(i+1)+"월"
    month_end[month] = end

print(month_end)
 '''

### 문자열
# 인덱싱 : 특정 위치의 문자 하나를 가져오는 것
# 슬라이싱 : 지정한 범위의 문자열을 가져오는 것
# 예제1
''' s='Hello'

print('result of length of s')
print(len(s))

print(s[1:len(s)])

print(s[3:len(s)]) '''

# 예제2
s = "안녕하세요"
''' print("s를 이루는 문자를 하나씩 출력, while")
i=0
while(len(s)):
    print(s[i])
    i+=1
    if i==5:
        break '''


''' print("s를 이루는 문자를 역순으로 하나씩 출력, while")
i=len(s)-1
while(1):
    print(s[i])
    i-=1
    if i<0:
        break '''


''' print("s를 이루는 문자를 하나씩 출력, for")
for c in s:
    print(c) '''

# 예제3
s = "a안b녕c하d세e요f"

'''print("s를 이루는 문자 중에서 한글만 출력, for, if or, continue")
for c in s:
    if c == 'a' or c=='b' or c=='c' or c=='d' or c=='e' or c=='f':
      continue
    print(c)
 '''

''' print("s를 이루는 문자 중에서 한글만 출력, for, if and, continue")
for c in s:
    if c != 'a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f':
      print(c)
 '''

''' print("s를 이루는 문자 중에서 한글만 출력, for, not in, 방법 3")
for c in s:
    if c not in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(c) '''


### 예외처리
# 예외
# - 프로그램 실행 중 발생하는 오류
# - 예외가 발생하고 처리되지 않으면 프로그램이 중단된다.
# - ex) 숫자가 아닌 문자열을 정수로 변환하는 경우

# 예외처리 방법
# - try, except 등을 사용하여 예외처리함.

''' num=int('abc') # Value error occur!!
print(num) '''

# try
# - 예외가 발생할 가능성이 있는 코드를 작성하는 영역
# - try 내부서 예외가 발생하면 이후 코드는 실행하지 않고, 
#   해당 예외를 처리할 수 있는 except 영역으로 이동한다.

# except
# - try 영역에서 발생한 예외를 처리하는 영역
# - 지정한 예외 발생했을 때 실행 됨.

### Class

''' class Person:
    def hello(self):
        print('hi')

Curry = Person() # curry는 Person의 instance, curry가 Person을 참조
Curry.hello()

a = int(10)
print(a)
 '''


''' b=list(range(10))
b.append(10)
print(b)
print(type(b)) '''


''' class Person():
    def __init__(self, name, age, hobby):
        self.hello = "Hello"
        self.name=name
        self.age=age
        self.hobby=hobby

    def introduce(self):
        print(f"{self.hello}, I am  {self.age}years {self.name}")

curry=Person('curry', 40, 'exercise') # 이 때 __init__ method가 이미 실행됐다.
curry.introduce() '''

''' class Person:
    pass

jin=Person() #인스턴스 생성
jin.name='진' # 인스턴스를 생성한 뒤 속성 추가

print(jin.name) '''


# 클래스 속성
class Person:
    folder = []
    def add_files(self, file):
        self.folder.append(file)

jin = Person()
jin.add_files('txt')

kim = Person()
kim.add_files('img')

print(jin.folder)
print(kim.folder)

print('hi')

