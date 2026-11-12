import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print("===== 전체 출력 =====")
print(df)

# 열 하나씩 출력 # DataFrame이 아닌, 1차원 Series로 출력
print("\n===== 열 하나씩 출력 =====")
print(df['Name'])
print(df['Age'])
print(df['Sex'])

print("\n==== 타입 출력 =====")
print(type(df))         # DataFrame
print(type(df['Age']))  # Series

print("\n===== 이름이 Age인 Series 생성 =====")
ages = pd.Series([22,35,44], name='Age')
print(ages)


print("\n===== DataFrame에서 특정 열 꺼내기 =====")
print(df['Age'])

print("\n===== 기본 통계 함수 =====")
print("max : 최댓값")
print("최대 나이 : ", df['Age'].max())

print("max : 최솟값")
print("최대 나이 : ", df['Age'].min())

print("max : 평균값")
print("최대 나이 : ", df['Age'].mean())


print('요약 통계 정보 보기')
print(df.describe())

print('DataFrame의 전체 요약 정보')
print(df.info())

