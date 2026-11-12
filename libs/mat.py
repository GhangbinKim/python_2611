import matplotlib.pyplot as plt
# figure : 큰 도화지
# subplots : 도화지 원에 나눠진 작은 칸들

''' # 기본 스타일 적용

plt.style.use('default')

# y값 전달, x는 자동으로 0,1,2,3으로 설정
#plt.plot([2,4,6,8])

x=[2,4,6,8]
y=[1,3,5,7]
plt.plot(x, y)
plt.show() '''

fig = plt.figure()
''' 
fig.add_subplot(1, 2, 1)
fig.add_subplot(1, 2, 2)
 '''
''' 
fig.add_subplot(1, 2, 1)
fig.add_subplot(2, 2, 2)
 '''
## 이전 figure 닫기
#plt.close('all')

''' a1 = fig.add_subplot(1, 2, 1)
a2 = fig.add_subplot(1, 2, 2)
x = range(0, 10)
y = range(5, 15)
a1.plot(x, y, 'c*')

x = range(0, 50)
y = range(0, 50)
a2.plot(x, y, 'mp')


plt.show() '''


# 이전 figure 닫기
#plt.close('all')
plt.style.use('ggplot')
# 1행 1열짜리 영역에서 1번째 위치에 그래프 생성
a = fig.add_subplot(111)
x=[3, 4] # 막대의 위치(좌표 기준)
y=[1, 2]

labels = ['english', 'math']
colors = ['red', 'blue']

# 세로 막대
#a.bar(x, y, tick_label=labels, color=colors)

# 가로 막대
a.barh(x, y, tick_label=labels, color=colors)

plt.show()


