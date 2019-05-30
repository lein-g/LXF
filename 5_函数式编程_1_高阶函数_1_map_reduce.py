def f(x):
    return x**2


f(2)

l = [1, 2, 3, 4]
g = [f(n) for n in l]
list(g)
g = map(f, l)
next(g)

# 把str转换为int

#1
from functools import reduce
def fn(x, y):
    return x*10+y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
reduce(fn, map(char2num, '12345'))

#2
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
str2int('12345')

#3
def char3num(s):
    return DIGITS[s]

def str3int(s):
    return reduce(lambda x, y: x * 10 + y, map(char3num, s))
str3int('12345')

#4...
int('12345')


# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    nname=name[0].upper()+name[1:].lower()
    return nname
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数
# 把字符串'123.456'转换成浮点数123.456
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]    
    return reduce(fn, map(char2num, s.split('.')[0]))+reduce(fn, map(char2num, s.split('.')[1]))/(pow(10,len(s.split('.')[1])))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')