# -*- coding: utf-8 -*-

"""
Python的函数定义非常简单，但灵活度却非常大
除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
"""

# 位置参数
# 计算x2的函数：


def power(x):
    return x**2  # 参数x就是一个位置参数


# 当我们调用power函数时，必须传入有且仅有的一个参数x：
power(4)

# 可以把power(x)修改为power(x, n)，用来计算x的n次方


def power1(x, n):
    return x**n  # x和n，这两个参数都是位置参数


# 对于这个修改后的power(x, n)函数，可以计算任意n次方：
power1(5, 3)

# 默认参数
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：


def power2(x, n=2):
    return x**n


# 这样，当我们调用power(5)时，相当于调用power(5, 2)
power2(5)
power2(5, 3)  # 对于n > 2的其他情况，就必须明确地传入n

"""
设置默认参数时：
一是必选参数在前，默认参数在后，否则Python的解释器会报错
二是如何设置默认参数：当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面
默认参数降低了函数调用的难度
有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数
当不按顺序提供部分默认参数时，需要把参数名写上
"""

# 默认参数有个最大的坑


def add_end(L=[]):
    L.append('end')
    return L


add_end([1, 2, 3])
add_end()  # 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 我们可以用None这个不变对象来实现：


def add_end1(L=None):
    if L == None:
        L = []
    L.append('end')
    return L


"""
为什么要设计str、None这样的不变对象呢？
因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误
此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有
我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象
"""

# 可变参数
# 顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
# 这些可变参数在函数调用时自动组装为一个tuple

# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum


calc([1, 2, 3, 7])
calc((1, 2, 5, 7))

# 如果利用可变参数，调用函数的方式可以简化


def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum


calc1(1, 2, 5, 7)
calc1()

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办
nums = [1, 2, 3]
calc1(nums[0], nums[1], nums[2])

# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
calc1(*nums)

# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

# 调用可以用简化
person('Jacl', 24, **extra)

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数

# 只接收city和job作为关键字参数


def person1(name, age, *, city, job):
    print(name, age, city, job)


person1('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了


def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，如果没有传入参数名，调用将报错
person2('Jack', 24, 'Beijing', 'Engineer')

# 命名关键字参数可以有缺省值，从而简化调用


def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person3('Jack', 24, job='Engineer')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*nums):
    p = 1
    if len(nums) == 0:
        raise TypeError('请至少输入一个参数')
    for n in nums:
        if not isinstance(n, (int, float)):
            raise TypeError('请输入int or float type的参数')
        else:
            p *= n
    return p


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

"""
小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误

要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict

以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
"""