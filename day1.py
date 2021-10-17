'''
#华氏改摄氏
f= float(input('f='))
c=(f-32)/1.8
print('%.1f华氏度=%.1f摄氏度'%(f,c))

#圆的半径计算周长和面积

radius=float(input('r='))
per=2*3.14*radius
area=3.14*radius*radius
print('周长per=%.3f'%per)
print('面积area=%.3f'%area)
'''


#是否为闰年
year=int(input('year='))
runyear = year%4==0 and year%100!=0 or year%400==0
print(runyear)