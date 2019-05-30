# -*- coding: utf-8 -*-

# 用print()在括号中加上字符串，就可以向屏幕上输出指定的文字
print('hello, world')

# print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')

# print()也可以打印整数，或者计算结果
print(300)
print(100 + 200)

print('100 + 200 =', 100 + 200)


# Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里
name = input('please enter your name: ')
print('Hello,', name)

"""
任何计算机程序都是为了执行一个特定的任务，有了输入，用户才能告诉计算机程序所需的信息，有了输出，程序运行后才能告诉用户任务的结果
输入是Input，输出是Output，因此，我们把输入输出统称为Input/Output，或者简写为IO
input()和print()是在命令行下面最基本的输入和输出
"""

# -*- coding: utf-8 -*-
print('1024*768 =', 1024*768)
