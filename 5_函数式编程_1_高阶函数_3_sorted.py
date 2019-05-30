# -*- coding: utf-8 -*-
"""
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
"""

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# def by_name(t):
#     n = t[0]
#     return n


# L2 = sorted(L, key=by_name)
# print(L2)


def by_score(t):
    n = t[1]
    return n


L2 = sorted(L, key=by_score)
print(L2)
