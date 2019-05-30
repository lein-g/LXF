"""
装饰器(Decorators)是 Python 的一个重要部分
简单地说：他们是修改其他函数的功能的函数
他们有助于让我们的代码更简短，也更Pythonic（Python范儿）

装饰器本质上是一个 Python 函数或类，
它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，
装饰器的返回值也是一个函数/类对象
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计
有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码到装饰器中并继续重用
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
"""


# 函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数


def now():
    print('2019-05-28')


f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

"""
假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
本质上，decorator就是一个返回函数的高阶函数
"""

# 定义一个能打印日志的decorator
# log是一个decorator，所以接受一个函数作为参数，并返回一个函数


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


"""
由于log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用
在wrapper()函数内，首先打印日志，再紧接着调用原始函数
"""


@log  # 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
def now():
    print('2019-05-28')


now()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
# 它实际上是对原有装饰器的一个函数封装，并返回一个装饰器
# 我们可以将它理解为一个含有参数的闭包
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 3层嵌套的decorator用法如下
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。


@log('execute')
def now():  # 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)
    print('2015-3-25')


now()

# 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
now.__name__

# 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错

import functools

def log(func):
    @functools.wraps(func)  # Python内置的functools.wraps就是干这个事的
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start_time=time.time()
        func=fn(*args,**kw)
        end_time=time.time()
        print('%s executed in %s ms' % (fn.__name__, end_time-start_time))
        return func
    return wrapper

# 测试1
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

