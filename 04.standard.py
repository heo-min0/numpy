import numpy as np

'''
평균 175 177 179 181 183  5개 평균값 179
분산 데이터들의 변경된 값이 퍼져있는 정도, 값이 들쑥날쑥 하면 분산 값이 커진다
        전부 평균값으로 뺀다
        175 177 179 181 183
        -4  -2  0   2   4
        16   4  0   4  16  5개 평균값이 분산 8 (최고값과 최저값의 차이와 값이 비슷하다)

표준편차 분산 값을 제곱근으로 해서 줄인 값
        sqrt(8) 2.828
'''
heights = [175,177,179,181,183]
print(heights)
h = np.array(heights)
print(h)

avg = np.mean(h) #평균
print(avg)

std = np.std(h) #표준편차
print(std)




    
