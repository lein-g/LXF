# -*- coding: utf-8 -*-

"""
list
Python内置的一种数据类型是列表：list
list是一种有序的集合，可以随时添加和删除其中的元素
"""

# 变量classmates就是一个list
classmates = ['Michael', 'Bob', 'Tracy']

# 用len()函数可以获得list元素的个数：
len(classmates)

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
classmates[0]
classmates[1]
classmates[2]
classmates[3]  # 当索引超出了范围时，Python会报一个IndexError错误
classmates[-1]
classmates[-2]
classmates[-3]
classmates[-4]  # 越界

# list是一个可变的有序表
# 可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']  # 二维数组，类似的还有三维、四维……数组
len(s)

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
l = []
len(l)

"""
tuple
另一种有序列表叫元组：tuple
tuple和list非常类似，但是tuple一旦初始化就不能修改
因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
"""

# tuple没有append()，insert()这样的方法
# 其他获取元素的方法和list是一样的
classmates = ('Michael', 'Bob', 'Tracy')

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)

# 如果要定义一个空的tuple，可以写成()
t = ()
print(t)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1)
print(t)  # 定义的不是tuple，是1这个数，这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号
t = (1,)
print(t)  # Python在显示只有1个元素的tuple时，也会加一个逗号,

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])  # 定义的时候tuple包含的3个元素
t[2][0] = 'X'
t[2][1] = 'Y'  # 把list的元素'A'和'B'修改为'X'和'Y'
print(t)  # 变的不是tuple的元素，而是list的元素，list本身是可变的

# 练习
# 请用索引取出下面list的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# 另，简便的方法
print(L[0][0],L[1][1],L[2][2], sep = "\n")

"""
小结
list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们
"""