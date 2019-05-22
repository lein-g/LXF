import os
g = (d for d in os.listdir('.'))
for n in g:
    print(n)

# 斐波拉契数列（Fibonacci）
# 除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        # print(b)
        yield b
        a, b,  = b, a+b
        n = n+1
    # 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
    return 'done'


g = fib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1


def yang(max):
    l = [1]
    n = 0
    while n < max:
        yield l
        g = [l[i]+l[i+1] for i in range(0)]
        l = [1]+g+[1]
        n = n+1


g = yang(1)
for n in g:
    print(n)
