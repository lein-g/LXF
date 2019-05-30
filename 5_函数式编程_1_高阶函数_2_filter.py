"""
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
"""


def is_odd(n):
    # 在一个list中，删掉偶数，只保留奇数
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]


def not_empty(s):
    # 把一个序列中的空字符串删掉
    # return s.strip()
    return s and s.strip()


list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']


# 计算素数的一个方法是埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

"""
Iterator是惰性计算的序列，
所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，
而代码非常简洁
"""

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
# 利用filter()筛选出回数


def is_palindrome(n):
    return n == int(str(n)[::-1]) 
    #第一个：代表选取所有元素，第二个“:-1”代表跳步数，若是:2就代表每两个取一个值，而:-1比较特殊，代表从末尾往前取（每一个取一个值就算是全取。。），结果就是倒序


# 测试:
output = filter(is_palindrome, range(1, 200))
print('1~200:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
