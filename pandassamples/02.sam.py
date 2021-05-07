import pandas as pd

data = [10,20,30,40,50]

ser = pd.Series(data)

ser[1] = 200
print(ser)
print(ser[:4])

data = {
    'one':'일',
    'two':'이',
    'three':'삼'
}
ser = pd.Series(data)
print(ser['two']) # 키값 또는 인덱스로 접근 가능
print(ser[0:2]) # 인덱스는 전까지, 키값은 포함

data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래', '이상민', '김수경'],
    'kor':[90, 80, 70, 70, 60, 70],
    'eng':[99, 98, 97, 46, 77, 56],
    'mat':[90, 70, 70, 60, 88, 99],
}
df = pd.DataFrame(data)
print( df.head() ) # 앞 5명의 데이터
print( df['name'] )
print( df.columns )

# iloc
print( df.iloc[0,1] )
print( df.iloc[2:4,2:4] )

# loc
print( df.loc[0,'name'] )
print( df.loc[:,'name':'eng'] )
print( df.loc[:,['name','eng']] )
print( df.loc[1::2,:] )
print( df.loc[[1,3,5],:] )

data = {
    'class1': {
        'name':['홍길동','성춘향','장길산'],
        'height':[173,165,180]
    },
    'class2': {
        'name':['임꺽정','홍경래','김수경'],
        'height':[188,155,169]
    }
}
panel = pd.Panel(data)
print(panel)

print(panel['class1'])

df = panel['class1']
print(df.iloc[0,0])

for key in panel:
    item = panel[key]
    for col in item.columns:
        for row in item[col]:
            print(row, end=' ')
        print()