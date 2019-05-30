# -*- coding: utf-8 -*-

"""
条件判断
计算机之所以能做很多自动化的任务，因为它可以自己做条件判断
"""

# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
age = 3
print('your age is', age)
if age >= 18:
    print('adult')
else:
    print('teenager')

# 可以用elif做更细致的判断
# if语句执行有个特点，它是从上往下判断，
# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 3
if age >= 18:
    print('adult')
elif age >= 6:  # elif是else if的缩写，可以有多个elif
    print('teenager')
else:
    print('kid')

# if判断条件还可以简写
x = []
if x:  # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
    print('True')
else:
    print('Flase')


# 再议 input
s = input('birth:')
try:  # int()函数发现一个字符串并不是合法的数字时就会报错，检查并捕获程序运行期的错误，稍超前
    b = int(s)  # input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
    if b < 2000:
        print('00前')
    else:
        print('00后')
except ValueError as e:
    print('error:', e)
    print('please input number')


# 练习
# 小明身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# height = 1.75
# weight = 80.5
height_str = input('请输入你的身高（单位：m）')
weight_str = input('请输入你的体重（单位：kg）')
height = float(height_str)
weight = float(weight_str)
bmi = weight/(height**2)
print('你的bmi指数为体重（%s kg）除以身高（%s m）的平方：%.2f' % (weight, height, bmi))
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

"""
小结
条件判断可以让计算机自己做选择，Python的if...elif...else很灵活
条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行
"""
