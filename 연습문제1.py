import numpy as np
# 문제1) ndarray 타입으로 3 by 4의 배열을 만들고 정수값(1~100)으로 랜덤하게 채운다음 
# 다음 출력들을 실행해보세요 
arr = np.random.randint(1,101,size=(3,4))
print(arr)

# 문제2) 행 출력하기 
print( arr[::1,] )

# 문제3)열 출력하기 
print( arr[::,::1] )

# 문제4)행의 누적합계 구하기 
print(arr.sum(axis=1))
print(arr.cumsum(axis=0))
# 문제5)열의 누적합계 구하기 
print(arr.sum(axis=0))

# 문제6) n1을 파일로 저장하기 
np.savetxt('n1.txt', arr)
#np.savetxt('n1.npy', arr) 배열저장
# load - 데이터 읽어오기 
print( np.loadtxt('n1.txt') )
#print( np.load('n1.txt') ) 로드로 불러오면 됨