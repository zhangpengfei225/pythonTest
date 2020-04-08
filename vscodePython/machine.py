import numpy as np
lis = [1,2,3]
#tile函数是将原lis分别在列上扩展3次，行上扩展4次
result = np.tile(lis,(3,4))
print(result)
#对应列位置进行相加返回的列表的长度是等于原二位列表的行数
print(result.sum(axis=1))
print(result.sum(axis=0))
#argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出到y。
print(result.sum(axis=0).argsort())
lis2 = [1,2,3]
nplist = np.array(lis2)
print(nplist)
#对于numpy对象列表，**2，直接可以实现numpy中的列表中的每一个元素都进行平方
print(nplist**2)
print(nplist**3)
# operator.itemgetter函数
# operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），下面看例子。

# a = [1,2,3] 
# >>> b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
# >>> b(a) 
# 2 
# >>> b=operator.itemgetter(1,0)  //定义函数b，获取对象的第1个域和第0个的值
# >>> b(a) 
# (2, 1)

# 要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。

# sorted函数
# Python内置的排序函数sorted可以对list或者iterator进行排序，官网文档见：http://docs.python.org/2/library/functions.html?highlight=sorted#sorted，该函数原型为：

# sorted(iterable[, cmp[, key[, reverse]]])

# 参数解释：

# sorted函数也可以进行多级排序，例如要根据第二个域和第三个域进行排序，可以这么写：
# sorted(students, key=operator.itemgetter(1,2))

# 即先跟句第二个域排序，再根据第三个域排序。

#首先ones这个函数是用来创建元素为1的矩阵的，第一个参数表示要创建的行数，第二个参数表示要创建的列数
weights = np.ones((5,2))
print(weights)
