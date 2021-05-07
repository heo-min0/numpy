
'''
Pandas
파이썬 계열의 엑셀
구조화된 데이터를 가공하여 데이터 분석, 통계처리 할 수 있는 라이브러리(modul)

Series 1차배열

DataFrame 2차배열

Panel 3차배열

'''
import pandas as pd

#list를 사용하여 시리즈
data = [10,20,30,40,50]
#data = {'a':1,'b':2,'c':3,'d':4,'e':5}

series = pd.Series(data)
print(type(series))
print(series) # 인덱스가 아닌 키값

print( data[0] ) # indexing
print( data[1:4] ) # 슬라이싱
#print( series['b':'d'] )

print('합계:',series.sum())
print('평균:',series.mean())
print('표준편차:',series.std())
print('최대값:',series.max())
print('최소값:',series.min())
print('중간값:',series.median())

# dict : 
data = {
    'name':['홍길동','임꺽정','장길산','홍경래'],
    'kor':[90,80,70,70],
    'eng':[99,98,97,68],
    'mat':[90,70,70,60]
}

df = pd.DataFrame(data)
print(type(df))
print(df)


# Panel (3,2,3)
array = [
            [ [1,2,3], [4,5,6] ],
            [ [7,8,9], [10,11,12] ],
            [ [13,14,15], [16,17,18] ]
        ]

array = pd.Panel(array)
print(type(array))
print(array)





