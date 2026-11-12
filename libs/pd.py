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

print('DataFrame에서 특정 행을 선택하는 방법 2가지')
# iloc
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

# loc : 'index 라벨'로 접근
print(df.loc[0])
print(df.loc[1])
print(df.loc[2])

print('\n=== 상위/하위 데이터 출력 ===')
# 상위 5개
print(df.head())
# 상위 2개
print(df.head(2))

# 하위 5개
print(df.tail())
# 하위 2개
print(df.tail(2))

print("\n ===== 열 수정 =====")
# 새로운 열 추가
df['Survived'] = [0, 1, 1]
print(df)

# 열 이름 바꾸기
df = df.rename(columns={'Sex' : 'Gender'})
print(df)

# 열 삭제하기(axis=1 : 열 / axis=0 : 행)
df = df.drop('Survived', axis=1)
print(df)


print('\n === 결측치(NaN) 처리 ===')
print(df)
print(df.isnull())

df2 = df.copy()

df2.loc[1, 'Age'] = None
print(df2)
print(df2.isnull())

print(df2.dropna(axis=0))

print(df2.fillna(0))

print(df2['Age'].fillna(df2['Age'].mean()))

print(df2.ffill()) # 바로 위(이전 행)의 값으로 NaN을 채운다. 
print(df2.bfill()) # 바로 아래(다음 행)의 값으로 NaN을 채운다. 