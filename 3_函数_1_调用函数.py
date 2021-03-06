# -*- coding: utf-8 -*-

"""
抽象
抽象是数学中非常常见的概念
计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，
于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作：
100
∑n
n=1
这种抽象记法非常强大，因为我们看到 ∑ 就可以理解成求和，而不是还原成低级的加法运算
而且，这种抽象记法是可扩展的
100
∑(n2+1)
n=1
还原成加法运算就变成了：
(1 x 1 + 1) + (2 x 2 + 1) + (3 x 3 + 1) + ... + (100 x 100 + 1)
借助抽象，我们才能不关心底层的具体计算过程，而直接在更高的层次上思考问题
写计算机程序也是一样，函数就是最基本的一种代码抽象的方式
"""

"""
调用函数
Python内置了很多有用的函数，我们可以直接调用
要调用一个函数，需要知道函数的名称和参数
Python的内置函数官方网站:
https://docs.python.org/zh-cn/3/library/functions.html
"""

# 比如求绝对值的函数abs，只有一个参数
abs(100)
abs(-20)

# 通过help(abs)查看abs函数的帮助信息
help(abs)

# 如果传入的参数数量不对，会报TypeError的错误
abs(1, 2)  # 并且Python会明确地告诉你：abs()有且仅有1个参数

# 传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
abs('a')  # 会给出错误信息：str是错误的参数类型

# max()可以接收任意多个参数，并返回最大的那个
max(1, 2)
max(2, 3, 1, -5)

"""
数据类型转换
Python内置的常用函数还包括数据类型转换函数
"""

# int()函数可以把其他数据类型转换为整数
int('123')
int(12.34)

float('12.34')

str(1.23)
str(100)

bool(1) == bool(2)
bool('') == bool()
bool(0) == bool(None)

# 函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
a(-10)


# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
n2 = 1000

print(str(hex(n1)), str(hex(n2)), sep="\n")

"""
小结
调用Python的函数，需要根据函数定义，传入正确的参数
如果函数调用出错，一定要学会看错误信息
"""
