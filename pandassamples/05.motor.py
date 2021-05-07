import pandas as pd

data = pd.read_csv('pandassamples/data/auto-mpg.csv')

print(data.info())

'''
mpg             398 non-null float64  갤런당 마일
cylinders       398 non-null int64    실린더 수
displacement    398 non-null float64  배기량
horsepower      396 non-null float64  마력
weight          398 non-null int64    무게
acceleration    398 non-null float64  가속
model-year      398 non-null int64    모델연도
'''
#통계정보
print(data.describe())

#사분위수 4범위로 나눈다
import numpy as np
arr = np.array([1,3,3,3,4,4,4,6,6])

df = pd.DataFrame(arr)

#1단계:오름차순 정렬
#2단계:중앙값 구함
print(df.median())
#3단계:왼쪽 값의 중앙값을 구함
print(df.quantile(0.25))
print(df.quantile(0.5))

#3단계:오른쪽 값의 중앙값을 구함
print(df.quantile(0.75))
print(df.quantile(1.0))

data10 = data[10:20]
print(data10)

#실린더가 4개인 경우
print( data10[data10.cylinders==4] )
print( data10.cylinders==8 )
print( data10[ [True, False, True, True, False, False, True, False, False, False] ] )
print( data[data.mpg>=27] )

#모델이 70년대인것만 카운트
print( data[  data['model-year']==70]['mpg'].count() )

#모델이 80년도, 연비 평균
print( data[ data['model-year']==80 ]['mpg'].mean() )