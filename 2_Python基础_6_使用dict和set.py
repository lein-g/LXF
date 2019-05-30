# -*- coding: utf-8 -*-

"""
dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
使用键-值（key-value）存储，具有极快的查找速度
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的
假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，
这种方法就是在list中查找元素的方法，list越大，查找越慢
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字
无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢
这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value
"""

# 用Python写一个dict如下：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print(d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Jack'] = 90
d['Jack'] = 88
print(d['Jack'])

# 如果key不存在，dict就会报错：
d['Thomas']

# 要避免key不存在的错误，一是通过in判断key是否存在：
'Thomas' in d

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')  # 返回None的时候Python的交互环境不显示结果
d.get('Thomas', -1)

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)

"""
dict内部存放的顺序和key放入的顺序是没有
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少
所以，dict是用空间来换取时间的一种方法

dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了
这个通过key计算位置的算法称为哈希算法（Hash）
要保证hash的正确性，作为key的对象就不能变
在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key
而list是可变的，就不能作为key
"""

key = [1, 2, 3]
d[key] = 'a list'

"""
set
set和dict类似，也是一组key的集合，但不存储value
由于key不能重复，所以，在set中，没有重复的key

set和dict的唯一区别仅在于没有存储对应的value，
但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
"""

# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)  # 显示的顺序也不表示set是有序的

# 重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
s.add(4)
print(s)

# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合
# 因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

"""
再议不可变对象
对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
"""

# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a)

而对于不可变对象，比如str，对str进行操作：
a = 'abc'  # a本身是一个变量，它指向的对象的内容才是'abc'
a.replace('a', 'A')  # 调用方法replace是作用在字符串对象'abc'上的，创建了一个新字符串'Abc'并返回
print(a)  # 变量a仍指向原有的字符串'abc'

"""
小结
使用key-value存储结构的dict在Python中非常有用
选择不可变对象作为key很重要，最常用的key是字符串
"""

# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果
t1 = (1, 2, 3)
t2 = (1, [2, 3])
d = {}
d[t1] = 123
print(d)
d[t2] = 456
print(d)  # 报错

# 练习
# Python如何实现将列表：['a','a','b','a','b','c']输出为字典：{'a':3,'b':2,'c':1}
str_list = ['a', 'a', 'b', 'a', 'b', 'c']
str_list.sort()
dic = {}
for i in str_list:
    dic[i] = str_list.count(i)
print(dic)
