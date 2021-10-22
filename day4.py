#水仙花数			
'''
求个、十、百位数时，
百位数除100
十位数除10再取10余
个位数10取余

for num in range(100,1000):
	low = num%10
	mid = (num//10)%10   #注意整除
	high = num//100
	if num == low**3 + mid ** 3 + high ** 3:
		print(num)
'''

#正整数反转

'''
这段程序里，当num大于0之前，下面的数一直在运算，每次只输出一个单独的数字。
每次所求的都是最后一位。
然后将num除10取证，去掉最后一位

num=int(input('num='))
r_num=0;
while num>0:
	r_num=r_num*10+num%10
	num //=10
print(r_num)

#百钱百鸡问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
#取20,33的原因是 当超过这些数时，就会超过100元
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


  '''
#
'''
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

randint是不能随便变的

from random import randint

money=1000
while money>0:
	print('你的总资产为：',money)
	go_on=False
	while True:
		debt=int(input('你的下注是：'))
		if 0<debt<=money:
			break
	first =randint(1,6)+randint(1,6)
	print('玩家roll出了%d!'%first)
	if first==7 or first ==11:
		print('玩家胜利')
		money+=debt
	elif first==2 or first==3 or first==11:
		print('庄家胜利')
		money-=debt
	else:
		go_on=True
	while go_on:
		go_on=False
		current=randint(1,6)+randint(1,6)
		print('玩家roll出了%d!'%current)
		if current==7:
			print('庄家胜利')
			money-=debt
		elif current==first:
			print('庄家胜利')
			money-=debt
		else:
			go_on=True
print("没钱啦，歇啦！")	


'''

'''
生成斐波那契数列的前20个数。

'''
'''
n=int(input('你想要几项？：'))
n1=1
n2=1
count=2

if n<=0:
	print('给个正整数，谢谢')
elif n==1:
	print('斐波那契数列')
	print(n1)
else:
	print('斐波那契数列')
	print(n1,',',n2,end=',')
	while count<n:
		nth=n1+n2
		print(nth,end=',')
		n1=n2
		n2=nth
		count+1

#这个代码用不了，时间复杂度太大了
		'''
class Fibonacci(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n:int 指 生成数列的个数
        """
        self.n = n
        # 保存当前生成到的数据列的第几个数据，生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__ 返回自身即可"""
        return self


if __name__ == '__main__':
    fib = Fibonacci(15)
    for num in fib:
        print(num)		