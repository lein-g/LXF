# -*- coding: utf-8 -*-
import math

"""
定义函数
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，函数的返回值用return语句返回

函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
return None可以简写为return
"""

# 自定义一个求绝对值的my_abs函数为例：


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))

# 如果想定义一个什么事也不做的空函数，可以用pass语句：


def nop():
    pass  # pass语句什么都不做，可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来

# pass还可以用在其他语句里，比如：


age = 20
if age >= 18:
    pass  # 缺少了pass，代码运行就会有语法错误

"""
参数检查
"""

# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
my_abs(1, 2)

# 但是如果参数类型不对，Python解释器就无法帮我们检查
my_abs('A')  # my_abs没有参数检查，会导致if语句出错
abs('A')  # 内置函数abs会检查出参数错误

# 修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数
# 数据类型检查可以用内置函数isinstance()实现：


def my_abs1(x):
    if not isinstance(x, (float, int)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


my_abs1('A')

"""
返回多个值
"""

# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值
r = move(100, 100, 60, math.pi / 6)
print(r)

# 返回值是一个tuple
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

"""
小结
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None
函数可以同时返回多个值，但其实就是一个tuple
"""

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 两个解
# 计算平方根可以调用math.sqrt()函数：


def quadratic(a, b, c):
    if b**2-4*a*c < 0:
        print('此方程无解')
    elif a == 0:
        print('次方程有唯一解x= ', -c/b)
    elif b**2-4*a*c == 0:
        print('次方程有唯一解x= ', -b/(2*a))
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        print('次方程的两个解为x1=%d,x2=%d' % (x1, x2))
        return x1, x2

quadratic(1,2,1)
quadratic(0,2,2)

# 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
