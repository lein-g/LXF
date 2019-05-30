"""
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
"""

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
# 调用函数f时，才真正计算求和的结果


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

"""
我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力
"""

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

"""
当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
"""

# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


print(count())
f1, f2, f3 = count()  # count()的返回值为三个闭包（i*i）组成的数据
print(f1())

# 再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数


def createCounter():
    def counter():
        return 1
    return counter


# 测试:
# 方法一：
# 定义变量n用于count，但由于n为不可变对象，
# 在当前作用域中的给变量赋值时，该变量将成为该作用域的局部变量，并在外部范围中隐藏任何类似命名的变量
# 所以访问外层函数的局部变量时， 要用nonlocal

def createCounter():
    n = 0

    def count():
        nonlocal n  # 使用外层变量
        n = n+1
        return n
    return count

# 方法二：
# 定义变量li用于count，list为可变对象
# 改变其元素【0】的值时，li本身并没有改变
# 内部函数可以使用外部函数的参数和局部变量，所以不需要使用nonlocal


def createCounter():
    li = [0]
    # print(id(li))

    def counter():
        li[0] += 1
        # print(id(li))
        return li[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
