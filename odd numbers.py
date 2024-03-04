input('Write ten integer numbers *after pressing enter*')

num1 = int(input('1)  '))
num2 = int(input('2)  '))
num3 = int(input('3)  '))
num4 = int(input('4)  '))
num5 = int(input('5)  '))
num6 = int(input('6)  '))
num7 = int(input('7)  '))
num8 = int(input('8)  '))
num9 = int(input('9)  '))
num10 = int(input('10) '))

maxnum = 0 

if (num1 % 2) == 1:
    maxnum = num1

if (num2 > num1) and ((num2 % 2) == 1):        
    maxnum = num2

if (num3 > maxnum) and ((num3 % 2) == 1):
	maxnum = num3

if (num4 > maxnum) and ((num4 % 2) == 1):
	maxnum = num4

if (num5 > maxnum) and ((num5 % 2) == 1):
	maxnum = num5

if (num6 > maxnum) and ((num6 % 2) == 1):
	maxnum = num6

if (num7 > maxnum) and ((num7 % 2) == 1):
	maxnum = num7

if (num8 > maxnum) and ((num8 % 2) == 1):
	maxnum = num8

if (num9 > maxnum) and ((num9 % 2) == 1):
	maxnum = num9

if (num10 > maxnum) and ((num10 % 2) == 1):
	maxnum = num10

print("The larger odd number of those entered, is ", maxnum)
