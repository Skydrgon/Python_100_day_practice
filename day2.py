'''
#英制单位英寸公制单位厘米互换。

a=float(input('请输入长度:'))
unit=input('请输入单位，in/英寸 还是 cm/厘米？ ')
if unit== 'in' or unit == '英寸':
	print('%f英寸=%f厘米'%(a,a*2.54))
elif unit == 'cm' or unit == '厘米':
	print('%f厘米=%f英寸'% (value,value/2.54))
else:
	print('您搁这儿打啥呢？')


#百分制转换为等级制
score=float(input("输入成绩："))
if score>=90:
	grade='A'
elif score>=80:
	grade='B'
elif score>=70:
	grade='C'
elif score>=60:
	grade='D'
else:
	grade='E'
print("对应等级：",grade)

'''

#输入三条边长，如果能构成三角形就计算周长和面积。

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if a+b>c and a+c>b and b+c>a:
	print('周长：%f'%(a+b+c))
	p=(a+b+c)/2
	area=(p*(p-a)*(p-b)*(p-c))**0.5
	print('面积:%f'%(area))
else:
	print('不能构成三角形')



