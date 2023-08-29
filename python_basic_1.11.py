
#   Homework 11.6.1

# When paying for purchases with a card abroad, banks make a conversion through an intermediate currency. For example, if you pay for goods in euros with a domestic card, then first this amount is converted into dollars, and then into rubles.
#
# Write a program that receives the purchase price in euros as input, and then outputs the answer in rubles. Let's imagine that we live in an alternative reality, where 1 euro = 1.25 dollars, and 1 dollar = 60.87 rubles.


cost=int(input('Enter cost of product in Euro:'))
dollr=1.25
rubl=60.87
cost_dollar=cost*1.25
cost_rubl=round(cost_dollar*60.87,2)
print('Cost of prroduct-',cost_rubl,'rubl')

# Homewor 11.6.2


# In one center of mathematical analysis, there was an intern who wrote programs for calculating functions. Once he was very tired and misunderstood the terms of reference, so the functions began to be roughly calculated.
#
# His program works as follows: a sequence of N real numbers is entered, while positive numbers are rounded up, and negative numbers are rounded down.
#
# Write a program that prints the natural logarithm of a number if it is positive, and the exponent to the power of the number if it is negative.
#
# Example:
#
# Enter number of numbers: 3
#
# Enter number: 1.3
#
# x = 2 log(x) = 0.6931471805599453
#
# Enter number: -2.1
#
# x = -3 exp(x) = 0.049787068367863944
#
# Enter number: -5.9
#
# x = -6 exp(x) = 0.0024787521766663585


import math
numbers=int(input('Enter amount of number:'))
for  i in range(1,numbers+1):
     number=float(input('Enter number:'))
     if number>0:
         number_ceil=math.ceil(number)
         number_log=math.log(number_ceil)
         print('x=',number_ceil,'log',number_ceil,'=',number_log)
     else:
       number_floor=math.floor(number)
       number_exp=math.exp(number_floor)
       print('x=',number_floor,'exp',number_floor,'=',number_exp)

#  Homework 11.10.3

# You are writing an installer for a computer game. While the installer is downloading the update, it is necessary for the user to display the percentage of downloaded percentages so that he understands whether he will have time to brew tea before the process is completed. Each game update requires a different amount of megabytes, while different players have different Internet connection speeds.
#
# Write a program that takes as input the size of the update file in megabytes and the speed of the Internet connection in megabytes per second. For every second, the program should calculate and display the percentage of the downloaded volume until the download is complete. At the end, the program should show how many seconds it took to download the update. Provide input control.
#
# Example:
#
# Specify file size for download: 123
#
# What is your connection speed: 27
#
# 1 sec has passed. Downloaded 27 out of 123 MB (22%)
#
# 2 seconds have passed. Downloaded 54 out of 123 MB (44%)
#
# 3 seconds have passed. Downloaded 81 out of 123 MB (66%)
#
# 4 seconds have passed. Downloaded 108 out of 123 MB (88%)
#
# 5 seconds have passed. Downloaded 123 out of 123 Mb (100%)

file=int(input('Enter amount of file:'))
speed=int(input('Enter speed of internet:'))
time=0
percentege=0
dowload=0
while dowload<file:
    time+=1
    dowload+=speed
    percentege+=round((speed/file)*100)
    if dowload > file :
      dowload=file
    percentege=round(dowload/file*100)

    print(time, '-second', dowload, 'dowloaded from', file, 'mg', (percentege),'%')


# Homework 11.10.4

# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки. При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками.

number=float(input('Enter number:'))
z=number//1
x=number-z
c=x*10
y=c//1
print(round(y))



# Homework 11.10.5

# For a term paper in physics, Andrey needs to compare the volumes of two planets: the Earth and a planet theoretically possible for our universe. Andrei is well versed in formulas, but he does not count well. The volume of the Earth is known to him - it is 1.08321 * 10 ** 12 km3.
#
# He needs to calculate the volume of a theoretically possible planet. It has a formula:
#
#  V=4/3*p*R**3
#
# In it, V is the volume, p is the number of pi, and R is the radius of the planet.
#
# Write a program that takes the radius of a random planet as input and displays how many times the planet Earth is smaller or larger than the theoretically possible planet in terms of volume. Round your answer to three decimal places.
#
# Example 1:
#
# Enter the radius of a random planet: 3389.5
#
# The volume of the planet Earth is 6.641 times larger
#
# Example 2:
#
# Enter the radius of a theoretically possible planet: 7000
#
# The volume of the planet Earth is less than (1/0.754) = 1.326 times

radius=float(input('Enter radius of planet:'))
v=(4/3)*3.14*(radius)**3
x=(10.8321*10**11)
z=0
y=0
if v>x:
    z+=round(v/x,3)
    print('The volume of the planet Earth is',z, 'times smaller')
elif v<x:
    y+=round(x/v,3)
    print('The volume of the planet Earth is', y, 'times larger')


 #Homework 11.10.6

high=int(input('Enter highest line:'))
low=int(input('Enter lowest line:'))
step=int(input('Enter step:'))
faradey=32
y=0
for x in range(low,high+1,step):
   y=x*1.8+32
   print(x,'gradus selsy=',y,'gradus faradey')
if high%step!=0:
 print(high,'gradus selsy=',high*1.8+32,'gradus faradey')

# H0mework 11.10.7
print('Enter positoin of  horse:')
x_horse=float(input('>>'))
x_horse=int(x_horse*10)

y_horse=float(input('>>'))
y_horse=int(y_horse*10)
print()
print('Enter positoin of  point:')
x_way=float(input('>>'))
x_way=int(x_way*10)

y_way=float(input('>>'))
y_way=int(y_way * 10)

print()
print('The horse is in a cage',((x_horse),(y_horse)),'.Suggested displacement cage',((x_way),(y_way)),end='\n')
if (x_way-x_horse==2 and y_way-y_horse!=1) or (x_way-x_horse!=1 and y_way-y_horse== 2):
  print('Yes, the horse can go there')
else:
  print('No, the horse can not go there')

#Homework 11.10.8
a=int(input('Enter degrees:'))
hour=30
x=a//hour
z=a-(x*hour)
#for one minute, the hour arrow turns 0.5 degrees, and the minute arrow turns 6 degrees
c=(z/0.5)*6
print('Since the beginning of the last hour minute arrow turns',c,'degrees')

# Homework 11.10.9
import cmath
print('General form:-ax**2+bx+c=0')
a=float(input('Enter a(a!=0):'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print()
print('Real solution of equation')
if d>0:
    print('Type of roots:two distict real roots')
elif d==0:
   print('Type of roots:two equal real roots')
elif d<0:
    print('Type of roots:two comlex roots')
print('The solution are',(sol1),'and',(sol2))

# Homework 11.10.10
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
max=(a+b+abs(a-b))/2
print('Bigger number is',max)
