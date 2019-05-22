from collections import Iterable

isinstance('abc', Iterable)
isinstance([1, 2, 3], Iterable)
isinstance(123, Iterable)

for x, y in enumerate([1, 2, 3]):
    print(x, y)


def findMinAndMax(L):
    if not L:
        return (None, None)
    else:
        min = max = L[0]

    for l in L:
        if l < min:
            min = l
        if l > max:
            max = l
    return(min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
