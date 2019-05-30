# -*- coding: utf-8 -*-

"""
循环
为了让计算机能计算成千上万次的重复运算，我们就需要循环语句
"""

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
for x in range(11):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
# 比如我们要计算100以内所有奇数之和，可以用while循环实现
sum = 0
num = 1
while num < 100:
    sum = sum+num
    num = num+2
print(sum)

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello,', i)

# 在循环中，break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

"""
小结
循环是让计算机做重复任务的有效的方法
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环
这两个语句通常都必须配合if语句使用
break和continue会造成代码执行逻辑分叉过多，容易出错
大多数循环并不需要用到break和continue语句
"""