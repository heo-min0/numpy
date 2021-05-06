import numpy as np
 
a = np.array([1,2,3])
b = np.array([4,5,6])

# 각 요소 더하기 np.add(a,b)
c=a+b
print(c)  # [5 7 9]

# 각 요소 빼기 np.subtract(a,b) 
c=a-b
print(c)  # [-3 -3 -3]

# 각 요소 곱하기 np.multiply(a,b)
c=a*b
print(c)  # [4 10 18]
 
# 각 요소 나누기 np.divide(a,b)
c=a/b
print(c)  # [0.25 0.4 0.5]




# 0에서 8 사이의 값을 가진 3x3 행렬 만들기
arr = np.arange(9).reshape((3,3))
print(arr)

# 크기가 30 인 랜덤 벡터를 만들고 평균값을 구하기
arr = np.random.randn(30)
print(arr)
print( arr.mean() )
# 테두리가 1이고 내부가 0인 2D 배열 만들기
arr = np.ones( (10,10) )
arr[1:-1,1:-1] = 0
print(arr)
# 10 ~ 49 의 값으로 배열을 만들고 반전(첫 번째 요소가 마지막이 됨)된 배열을 작성하라.
arr = np.arange(10,50)
a = arr[::-1] # a = np.flip(arr)
print(a)
# 랜덤 값으로 3x3x3 배열 만들기
arr = np.random.randn(3,3,3)
print(arr)


# 다음 빈칸에 들어 갈 코드를 작성하라.
# 배열의 생성
x = np.linspace(1, 9, 9, dtype=int)
print(x)         # [1 2 3 4 5 6 7 8 9]

# 4                
print( x[3:9:9,] )
# [6 7]            
print( x[5:-2:,] )
# [7 8 9]           
print( x[-3::,] )
# [6 7 8 9]        
print( x[5::,] )
# [1 3 5 7 9]        
print( x[::2,] )
# [9 8 7 6 5 4 3 2 1]
print( x[::-1,] )
# [2 5]
print( x[1:7:3,] )
# 다음 코드를 확인해 보자.
x1 = x                # 얕은 복사
x2 = x[2:]            # 얕은 복사
x3 = np.copy(x)       # 깊은 복사
x4 = x[[0, 1, 2, 3]]  # 깊은 복사

x1[1] = 10    # x [1] = 10 이 된다
x2[2] = 11    # x[2] = 11에 대입되지 않음
x3[3] = 12    # x[3] = 12에 대입되지 않음
x4[3] = 13    # x[4] = 12에 대입되지 않음
print(x)      
print(x1)     
print(x2)     


# True 및 False 의한 데이터의 선택
x = np.linspace(1, 9, 9, dtype=int)
idx = x > 3 
print(idx)
print(x[idx])
			
# [5]
idx = x == 5
print(x[idx])
# [4 5 6 7 8]
idx = (3<x) & (x<9)
print(x[idx])
# [1 2 9]
idx = (3>x) | (x>8)
print(x[idx])
