'''
머신러닝:com에 훈련을 시킴
    Data    1 2     4
    Result  2 3     5
    지도학습
        Data > % > ?
    비지도학습


순서
1.Data준비
2.방법(알고리즘) 선택
3.전처리
    1) 필요한 데이터만 선별
    2) 수정작업
    3) 학습데이터/평가용 데이터를 분할
4.모델의 학습(트레이딩)
5.모델의 평가(조정)
6.최적 모델 산출
7.테스트

'SepalLength', 꽃받침 길이
'SepalWidth',  꽃받침 폭
'PetalLength', 꽃잎   길이
'PetalWidth',  꽃잎   폭

'''
import pandas as pd
from sklearn.model_selection import train_test_split #알고리즘
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score #정확도평가

#붓꽃 데이터 로드
iris_data = pd.read_csv('./pandassamples/data/iris.csv',encoding='utf-8')
print(iris_data)

#데이터 레이블을 입력 데이터로 분리
y = iris_data.loc[:,'Name']
x = iris_data.loc[:,'SepalLength':'PetalWidth'] #'SepalLength',  'SepalWidth',  'PetalLength',  'PetalWidth'
print(x)
print(y)

#학습용 및 데이터용으로 분리
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, train_size=0.7, shuffle=True)

#학습
clf = SVC()
clf.fit(x_train, y_train)

#평가
y_pred = clf.predict(x_test)
result = accuracy_score(y_test, y_pred)
print('정답률:',result)

#새로운 데이터를 입력
mydata = [ [5.2,3.0,1.5,0.6] ]
fname = clf.predict(mydata)
print(fname) #Iris-setosa



