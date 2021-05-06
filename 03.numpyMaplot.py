import numpy as np

X = np.linspace(-10,10,1000)
print(X)

y = np.sin(X)
print(y)

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
'''
fontprop = fm.FontProperties(fname='godoMaum.ttf',size=18)

plt.title('sin Wave 파동',fontProperties=fontprop)
plt.xlabel('X축',fontProperties=fontprop)
plt.ylabel('y축',fontProperties=fontprop)
plt.grid(True)
plt.plot(X,y)
plt.show()
'''
'''
np.random.seed(1) # 랜덤값 유지?
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.scatter(x, y)
plt.title('scatter')
plt.show()
'''
# np.savetxt 넘파일 전용 저장?
arr = np.random.randn(3,4)
print(arr)

# txt file
np.savetxt('array34.txt', arr)

a = np.loadtxt('array34.txt')
print(a)

#csv > 1 2 3 > 1,2,3
np.savetxt('arr34.csv', arr, delimiter=',')








