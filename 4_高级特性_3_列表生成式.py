import os
[d for d in os.listdir('.')]

d = {'x': '1', 'y': '2', 'z': '3'}
for k, v in d.items():
    print(k, '=', v)
[k + '=' + v for k, v in d.items()]

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
