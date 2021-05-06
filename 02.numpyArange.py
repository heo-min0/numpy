import numpy as np

# 0~19까지 4x5 배열작성
nArr = np.arange(20).reshape(4,5)
print(nArr)

# 1~2행, 2~3열
a = nArr[1:3,2:4]
print(a)

a = nArr[:2,1:]
print(a)

# 행 방향을 하나씩 넘어서
a = nArr[::2,:]
print(a)

# 행 역순
a = nArr[::-1,:]
print(a)

# 열 역순
a = nArr[::,::-1]
print(a)

# zeros, ones
print(np.zeros( (2,10) ))
print(np.ones( (3,5) ))

arr = np.array([1,2,3,4,5,6])
print(arr.shape)
print(arr.ndim) #차원?

arr = np.arange(6).reshape((3,2))
print(arr)
print(arr.ndim)

arr = np.array([arr,arr])
print(arr)
print(arr.shape)

print(arr.sum(axis=0)) #축의 모든 합계
print(arr.sum(axis=1)) #x축 합계
print(arr.sum(axis=2)) #y축 합계


arr = np.array([0,1,2])
print(arr.dtype)

arr = np.array([0,1,2], dtype='int64')
print(arr.dtype)

arr = np.array([3e50,4e35],dtype='float64')
print(arr.dtype)
print(arr)

arr = np.array([3.5,2.3,4.1],dtype='int')
print(arr)

arr = np.array([0,2,0,-4],dtype='bool')
print(arr)

#배열복사
arr = np.array([1,2,3])
viewArr = arr.view()
print(viewArr)

viewArr[1] = 200
print(arr) # 원본에 영향을 준다, 깊은복사
print(viewArr)

copyArr = arr.copy()
copyArr[1] = 222
print(arr) # 원본에 영향을 안준다, 얇은복사
print(copyArr)

