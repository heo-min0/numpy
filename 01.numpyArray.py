print('numpy test')

import numpy as np

arr = [1,2,3]
print(arr * 3)

nArr = np.array([1,2,3])
print(nArr * 3)

nArr2 = np.array([2,2,1])
print(nArr / nArr2)

nArr3 = np.dot(nArr, nArr2) #곱해서 더하기
print(nArr3)

nArr4 = np.arange(10) # 0~9까지 배열 만들기
nArr4 = np.arange(2,10,3)
print(nArr4)

nArr5 = np.linspace(0, 10, 15) # 0~10 사이를 15등분하기
print(nArr5)

# 2차원 배열
nArrar2 = np.array([ [1,2,3], [4,5,6] ]) #row - colum |
print(nArrar2)
print(nArrar2.shape) #배열의 정보 : 2행 3열

nArr = np.sum(nArrar2)
print(nArr)

nArr = np.sum(nArrar2,axis=1) #행의 합계
print(nArr)

nArr = nArrar2.reshape(3,2) #행과 열 수정
print(nArr)

nArrar3 = nArrar2.T #행과 열 전환
print(nArrar3)

nArrar4 = np.transpose(nArrar2) #행과 열 전환(numpy 전용함수)
print(nArrar4)

# Matrix 행렬
nArrar5 = np.random.randn()
print(nArrar5)

nArrar5 = np.random.rand() #0에서 1사이
print(nArrar5)

nArrar5 = np.random.randn(2,3) #2x3 배열생성
print(nArrar5)

nArrar6 = np.array([[1,2,3],[4,5,6]])
print(nArrar6[0,0])

nArrar6 = np.array([0,5,3,4,1])
print(nArrar6[1:3])
print(nArrar6[1:5:2]) # 범위를 2씩 건너뛰어서

nArrar7 = np.array([1,2,3])
nArrar8 = np.array([[1,2,3],[4,5,6]])
print(nArrar7.data ) #주소
print(nArrar8.flags ) #정보
print(nArrar8.size )
print(nArrar8.shape )


nArrar9 = np.array([[[1,1,1],[2,2,2],[3,3,3],[4,4,4]]])
print(nArrar9 )
print(nArrar9.shape )

nArrar1 = np.array([1,2,3])
nArrar2 = np.array([[1,1,1],[2,2,2]])

# broadcast 1대 다수의 연산
print(nArrar1+nArrar2)
print(np.array([1,2,3]) + [1])

arr1 = np.array([[2],[1]])
arr2 = np.array([[5]])
arr3 = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
    ])

print('1+2',arr1+arr2)
print('1+2+3',arr1+arr2+arr3)




