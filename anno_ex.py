### 어노테이션
# - 이 변수나 함수는 이런 타입이라고 설명해주는 일종의 표시.

# 기본 변수
age = 30

# 어노테이션 추가
age: int = 30

print(age)

## 함수 어노테이션
def add(a: int, b:int)->int:
    return a+b

print(add(3,5))
print(add('3', '5'))

## 리스트, 딕셔너리 어노테이션

nums = list[int] = [1,2,3] # 리스트 안에 int가 들어간다는 의미

person: dict[str, int] = {  # 딕셔너리 타입 지정
    'age' : 30,
    'height' : 170
}