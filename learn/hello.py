# demo1
# print("请输入第一个数")
# param1 = input()
# print("请输入第二个数")
# param2 = input()
# print("请输入第三个数")
# param3 = input()

# params = [param1, param2, param3]
# params.sort()
# print("自小到大排序如下：")
# for param in params:
# 	print(param)


#demo2
# print("请输入姓名：")
# name = input()
# print("请输入年龄：")
# age = input()
# print("请输入零钱：")
# money = input()
# content = '{0}s% 今年d%岁，有零钱{1}f%'.format(name,age, money)
# print(content)

#demo3
#注意：输入值默认为字符串，使用math需手动导包
# import math

# a = float(input()) 
# b = float(input())
# c = float(input())

# def f(a, b, c):
# 	print('进入函数')
# 	if(pow(b, 2) - 4 * a * c < 0):
# 		print("该方程没有实数解")
# 	if(pow(b, 2) - 4 * a * c == 0):
# 		print('该方程有两个相同的实数解')
# 		x = (-b + math.sqrt(pow(b, 2) - 4 * a * c))/(2 * a)	 
# 		print(x)
# 	if(pow(b, 2) - 4 * a * c > 0):
# 		print('该方程有两个不同的实数解')
# 		x = (-b + math.sqrt(pow(b, 2) - 4 * a * c))/(2 * a)
# 		y = (-b - math.sqrt(pow(b, 2) - 4 * a * c))/(2 * a)
# 		print(x, y)
# f(a, b, c)

#test:函数测试
#默认参数
# def caculate2(x, y = 1):
# 	return x + y
# result = caculate2(1)
# print(result)

#可变参数
# def caculate(*params):
# 	s = 0 
# 	for param in params:
# 		s = s + param
# 	return	s
# print(caculate(1,2)) 

#关键字参数
# def f1(name, age, **args):
# 	print(name, age, args)
# descs = {'desc1':'帅', 'desc2':'没钱'}
# print(descs['desc1'])
# f1('孙博文', 23, desc1='帅', desc2='没钱')
# f1('孙博文', 23, **descs)

#命名关键字参数
# def f2(name, age, *, money='23.22'):
# 	print(name, age, money)
# f2('孙博文', 23, money='11.12')
# f2('孙博文', [1, 2])
# def f3(name, age, *args, money='23.22'):
# 	print(name, age, args, money)
# f3('孙博文', 23, 1, 2, 3, money='11.12')

#demo4
# def product(x, *y):
# 	a = 1
# 	for i in y:
# 		a = a * i 
# 	return x * a
# print(product(1, 2, 3))

#demo5
# str1 = '   123456   ';
# def trim(str):
# 	while str[0] == ' ':
# 		str = str[1:]
# 	while str[-1] == ' ':
# 		str = str[:-1]
# 	return str
# print(trim(str1))

#demo6
# list1 =[1, 2, 3, 5]
# def findMaxAndMin(list):
# 	max = list[0]
# 	min = list[0]
# 	for x in list:
# 		if x > max:
# 			max = x
# 		if x < min:
# 			min = x
# 	return (max, min)
# print(findMaxAndMin(list1))
#扩展,冒泡排序
# def sort1(list):
# 	for
# 	for x in range(1, len(list1)):

#测试列表生成器
# list2 = [pow(x, 2) + y for x in range(0, 9) for y in range(1, 3)]
# print(len(list2))
# print(list2)		
#测试generator
# generator1 = (pow(x, 2) for x in range(0, 9))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# for x in generator1:
# 	print(x)
# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		print(b)
# 		a, b = b, a + b
# 		n = n + 1
# 	return 'done'
# fib(5)

#demo7(杨辉三角)
# def generator_DEMO7(max):
# 	list1 = [1]
# 	list2 = []
# 	yield list1
# 	j = 0
# 	while j < max:	
# 		i = 0		
# 		while i < (len(list1) + 1):
# 			if i == 0 or i == len(list1):
# 				element = 1
# 			else:
# 				element = list1[i - 1] + list1[i]
# 			list2.append(element)
# 			i += 1
# 		list1 = list2
# 		list2 = []
# 		j += 1 
# 		yield list1
		
# for n in generator_DEMO7(10):
# 	print(n)

#demo8
# word = 'bowensun'

# def caps(word):
# 	return word[0].upper() + word[1:].lower()

# list1 = ['adam', 'LISA', 'barT']
# print(list(map(caps, list1)))

#demo9
# number = 123454321

# def numberGenerator(max):
# 	i = 0
# 	while i < max:
# 		i += 1
# 		yield i 

# def is_palindrome(number):
# 	str1 = str(number)
# 	str2 = str1[:]
# 	list(str2).reverse()
# 	str2 = "".join(str2) 
# 	return str1 == str2 

# def palindromeGenerator(x):
# 	it = numberGenerator(x)
# 	while true:
# 		number = next(it)

# 		yield next(it)
# 		it = filter(is_palindrome(number), it)
# for x in palindromeGenerator(10000):
# 	print(x)

# generator1 = numberGenerator(100)


# list1 = list(filter(is_palindrome(next(generator1)), generator1)) 
# for x in list1:
# 	print(x)

#demo10
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sort(category):
	if category == 'score':
		L1 = sorted(L, key = tuple[1])
	if category == 'name':
		L1 = sorted(L, key = tuple[0].lower)

print(sort('score')) 
		