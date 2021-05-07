import pandas as pd


# 다음과 같이 출력되도록 작성하라
'''
   A   B    C     D
0  a  aa  aaa  aaaa
1  b  bb  bbb  bbbb
2  c  cc  ccc  cccc
3  d  dd  ddd  dddd
4  e  ee  eee  eeee
'''
'''
import numpy as np
arr = np.array('a')
for i in arr:
   arr.
'''
data = {
    'A':['a', 'b', 'c', 'd', 'e'],
    'B':['aa', 'bb', 'cc', 'dd', 'ee'],
    'C':['aaa', 'bbb', 'ccc', 'ddd', 'eee'],
    'D':['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee']
}
data1 = pd.DataFrame(data)
print(data1)
# pandas_train.csv을로드 변수 df에 저장하기
df = pd.read_csv('./pandassamples/data/pandas_train.csv')
print(df)

# df에 저장된 데이터를 pandas_train2.csv라는 파일명으로 출력하기
df.to_csv('pandas_train2.csv')


# pandas_train.csv의 Satisfied 열을 모두 0으로 변경
df['Satisfied'] = 0
print(df)


# PassengerId, Ticket하는 열을 제거
df.drop(['PassengerId'])



