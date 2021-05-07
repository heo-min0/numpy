import pandas as pd

#data = pd.read_csv('./pandassamples/data/score.csv')
#data = pd.read_csv(r'.\pandassamples\data\score.csv')
#data = pd.read_csv('.\\pandassamples\\data\\score.csv')

data = pd.read_csv('D:/numpysamples/pandassamples/data/score.csv')

print(type(data))
print(data)

data1 = pd.read_csv('./pandassamples/data/score_noheader.csv', header=None)
print(data1)
print(data1.columns)

data1.columns = ['name','kor','eng','mat',]
print(data1)

data1['total'] = data1['kor'] + data['eng'] + data['mat']
data1['avg'] = data1['total']/3
print(data1)

data1.to_csv('score_result2.csv',mode='w',encoding='cp949', index=False)



