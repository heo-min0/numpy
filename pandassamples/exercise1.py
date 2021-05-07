import pandas as pd

# pandas_train.csv을로드 변수 df에 저장하기
df = pd.read_csv('pandas_train.csv')
print(df)
# df 행과 열 개수를 표시한다
print(df.shape)

# df 열 이름의 목록을 출력
print(df.columns)

# df의 각 열 결손 값이 아닌 데이터의 수와 데이터 유형을 표시
print(df.info())

# df의 각 열 결손 치의 수를 표시(=null)
print(df.isnull().sum() )


# df의 각 수치 데이터의 요약 통계보기
print(df.describe())

# 만족도가 0인 데이터만 출력
print(df[ df['Satisfied']==0 ] )


# df의 Age 열과 Name 열만 표시
print( df.loc )


