

''' def outer():
    print("outer 함수 실행")

    def inner():
        print('inner 함수가 실행')

    return inner

func = outer()
func() '''

''' ### 클로저
# -클로저는 '외부 함수의 변수를 기억하는 내부 함수'
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수

    def multiplier(n):
        # 내부 함수 multiplier는 바깥 함수의 x를 사용할 수 있음.
        return x*n
    
    return multiplier

times3 = make_multiplier(3) # 매개변수 x에 3을 전달
print(times3(10))           # n에 10을 전달
print(times3(5))            # n에 5를 전달 
 '''
''' 
### 데코레이터 기본 구조
# 데코레이터 : 함수를 꾸며주는 함수

def decorator(func):
    # func는 꾸며줄 함수

    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')
    return wrapper

def  say_hello():
    print('안녕하세요.')

decorated = decorator(say_hllo)
decorated() '''

### 매개변수가 있는 데코레이터
def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')
    return wrapper

@decorator_width_args
def say_name(name):
    print('이름 : ', name)

say_name('홍길동')