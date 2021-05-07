import pandas as pd

data1 = {'kor':90,           'mat':80}
data2 = {'kor':90, 'eng':70 }
data3 = {'kor':90, 'eng':70, 'mat':80}

ser1 = pd.Series(data1)
ser2 = pd.Series(data2)
ser3 = pd.Series(data3)

# result = ser1+ser2+ser3
result = ser1.add(ser2, fill_value=0).add(ser3, fill_value=0)

print(result)
print(ser1 + 300)

data1 = {'kor':90, 'eng':90, 'mat':80}
data2 = {'kor':90, 'eng':70, 'mat':100}
data3 = {'kor':90, 'eng':70, 'mat':95}

data = pd.DataFrame()
data = data.append(data1, ignore_index=True)
data = data.append(data2, ignore_index=True)
data = data.append(data3, ignore_index=True)
print(data)

data['total'] = data.kor + data.eng + data.mat
data['avg'] = data.total / 3
print(data)

data = {
    'fruits':['망고','딸기','수박','파인애플'],
    'price':[2500,5000,10000,7000],
    'count':[5,2,2,4]
}
df = pd.DataFrame(data)

# 추가 append는 객체를 새로 받아야 한다?
df = df.append( {'fruits':'사과','price':3500,'count':10},ignore_index=True)
print(df)

# 삭제
df2 = df.drop('price',axis=1)
print(df2)

# 삭제(행:row)
df3 = df.drop(0,axis=0)
print(df3)
