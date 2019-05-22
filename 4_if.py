# -*- coding: utf-8 -*-

# 小明身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# height = 1.75
# weight = 80.5
height_str = input('请输入你的身高（单位：m）')
weight_str = input('请输入你的体重（单位：kg）')
height = float(height_str)
weight = float(weight_str)
bmi = weight/(height**2)
print('你的bmi指数为体重（%s kg）除以身高（%s m）的平方：%.2f' %(weight, height, bmi))
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
