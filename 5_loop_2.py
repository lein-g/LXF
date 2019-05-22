# 计算100以内所有奇数之和

n = 99
sum1 = 0
while n > 0:
    sum1 = sum1+n
    n = n-2
print(sum1)

sum2=0
for i in range(101):
    if i%2==0:
        continue
    else:
        print(i)
        sum2=sum2+i
print(sum2)