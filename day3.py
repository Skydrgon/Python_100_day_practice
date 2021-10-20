'''
输入一个正整数判断它是不是素数

当数不是素数是合数，那么一定可以由两个自然数相乘得到，其中一个大于或等于它的平方根，一个小于或等于它的平方根。并且成对出现
任一大于1的自然数，要么本身是质数，要么可以分解为几个质数之积，且这种分解是唯一的。

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(num**0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)



#输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

x=int(input('x='))
y=int(input('y='))
if x>y:
    x,y=y,x
for a in range(x,0,-1):
    if x%a==0 and y%a==0:
        print("%d和%d的最大公约数是%d"%(x,y,a))
        print("%d和%d的最小公倍数是%d"%(x,y,x*y//a))  #整除
        break
        

'''


#打印图案



row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
