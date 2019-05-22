str_list = ['a', 'a', 'b', 'a', 'b', 'c']
str_list.sort()
dic = {}
for i in str_list:
    dic[i] = str_list.count(i)
print(dic)
