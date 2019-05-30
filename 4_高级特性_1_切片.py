def trim(s):
    if not isinstance(s, str):
        raise TypeError('bad operand type')

    # 起始位开始第一位如果为空，第二位开始到结尾重新赋值，递归
    if s[:1] == ' ':
        return trim(s[1:])
    # 最后一位如果为空，起始位到倒数第二位重新赋值，递归
    if s[-1:] == ' ':
        return trim(s[:-1])
    return s


# 测试:
if trim('hello ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
