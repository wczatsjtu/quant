# ref:https://wizardforcel.gitbooks.io/python-quant-uqer/content/7.html

import numpy as np

print(np.version.full_version)

a = np.arange(20)
print(a)

a = a.reshape(4, 5)
print(a)

a = a.reshape(2, 2, 5)
print (a)

a.ndim

a.shape

a.size

print(a.dtype)

##创建数组

raw = [0,1,2,3,4]
a = np.array(raw)
print(a)

d = (4, 5)
print(np.zeros(d))

d = (4, 5)
np.ones(d, dtype=int)

np.random.rand(5)

## 数组操作

a = np.array([[1.0, 2], [2, 4]])
print("a:")
print(a)
b = np.array([[3.2, 1.5], [2.5, 4]])
print ("b:")
print (b)
print ("a+b:")
print (a+b)

print ("3 * a:")
print (3 * a)
print ("b + 1.8:")
print (b + 1.8)

a /= 2
print (a)


#开根号求指数也很容易：
print( "a:")
print (a)
print ("np.exp(a):")
print (np.exp(a))
print ("np.sqrt(a):")
print (np.sqrt(a))
print ("np.square(a):")
print (np.square(a))
print ("np.power(a, 3):")
print (np.power(a, 3))


#需要知道二维数组的最大最小值怎么办？想计算全部元素的和、按行求和、按列求和怎么办？for循环吗？不，NumPy的ndarray类已经做好函数了：

a = np.arange(20).reshape(4,5)
print ("a:")
print (a)
print ("sum of all elements in a: " + str(a.sum()))
print ("maximum element in a: " + str(a.max()))
print ("minimum element in a: " + str(a.min()))
print ("maximum element in each row of a: " + str(a.max(axis=1)))
print ("minimum element in each column of a: " + str(a.min(axis=0)))

#科学计算中大量使用到矩阵运算，除了数组，NumPy同时提供了矩阵对象（matrix）。矩阵对象和数组的主要有两点差别：一是矩阵是二维的，而数组的可以是任意正整数维；二是矩阵的*操作符进行的是矩阵乘法，乘号左侧的矩阵列和乘号右侧的矩阵行要相等，而在数组中*操作符进行的是每一元素的对应相乘，乘号两侧的数组每一维大小需要一致。数组可以通过asmatrix或者mat转换为矩阵，或者直接生成也可以：
a = np.arange(20).reshape(4, 5)
a = np.asmatrix(a)
print(type(a))

b = np.matrix('1.0 2.0; 3.0 4.0')
print(type(b))