# Homework 4.5.1

#What should be done
#
#Outside the window of the apartment there is a weather sensor that determines whether it rains. If it goes, the sensor announces the message: “Rain went. Take the umbrella! "
#
#Write a program that receives a number 0 or 1. Unit means that the rain is going on. In this case, bring the message to the screen: “Rain went. Take the umbrella! ” Zero means that there is no rain, in this case you need to display the message "No rain!"
#
#Example 1:
#It is raining outside? 1
#Rain is coming. Take an umbrella!
#Example 2:
#It is raining outside? 0
#There is no rain!

x=int(input('Add number:'))
if x==1:
   print('Its raining')
if x==0:
    print('Its not raining')





 # Homework 4.5.2

#What should be done
#
#Vasya works as a developer, and his company creates a site for an educational company. Customers asked to implement the exam calculator to help applicants. This task was given to Vasya.
#
#Write a program that requests the user's results of the exam in three exams, and checks whether he has entered the budget. The passage score is 270. Display the appropriate message.
#
#Example 1:
#Enter the number of points in the Russian language: 90
#Enter the number of points in mathematics: 90
#Enter the number of informatics points: 90
#Congratulations, you entered the budget!
#
#Example 2:
#Enter the number of points in the Russian language: 100
#Enter the number of points in mathematics: 50
#Enter the number of points in computer science: 70
#Unfortunately, you did not go to the budget.


russian=int(input('Score from russian:'))
math=int(input('Score from math:'))
IT=int(input('Score from IT:'))
if (russian+math+IT)>=270:
     print('You passed!')
else:
   print('Unfortunately you failed!')






# Homework 4.5.3

#What should be done
#
#After the task, Vasya was tired and realized that the next day he would have to restore strength. Vasya decided that he would work only on a single day and wrote a small program that would help him not miss the working day.
#
#Write a program that checks whether the user entered the number and displays the corresponding message.
#
#Hint: To check the chatter, use the operator %.

days=int(input('Add days:'))
if days%2==0:
    print('You need to work today!')
else:
    print('You can rest ')




#    Homework  4.5.4

#What should be done
#
#Vasin's friend moved to a new apartment, and he needs to buy three chairs in different rooms. The prices for chairs are different, and in some stores there are discounts. A friend wants to order a discount calculator from Vasya to be easier to navigate in prices.
#
#Write a program that requests three costs of goods and calculates the amount of the check. If the check amount exceeds 10,000 rubles, you need to subtract 10% discount from this amount (multiply by 10, divide by 100). The total amount should be displayed on the screen

stul_1=int(input('Add cash:'))
stul_2=int(input('Add cash:'))
stul_3=int(input('Add cash:'))
x=stul_1+stul_2+stul_3
if x>10000:
   print((x/100)*10)
else:
 print('You can buy them:')

 
 
 # Homework 4.5.5

#What should be done
#
#Create a program that will find a module for the next number X. If the number X is negative, then it must translate it into a positive one, and at the end there should be a module of the entered number on the screen.
#
#Example:
#Introduced 5, answer 5
#Introduced −7, answer 7
#Hint: In some cases, it is enough to re -provide a variable with a minus sign.

x=int(input('Add number:'))
if x<0:
 print('Modul of',x,'equal to',x*(-1))
else:
 print('Modul of',x,'equal to',x)

 
 
#  Homework 4.5.6
#
#Vasya understands how important rest is after a hard working day, so he often goes to a local bar with friends. The owner of the bar loves gambling and sometimes offers visitors to play with him. Vasya avoids gambling, but invited the owner to buy a program from him to calculate the results of the game, which can be displayed on the screens of the bar.
#
#Write the program: two numbers are submitted to the input in it. If the first number is larger or equal to the second, then you need to display their difference on the screen and a separate line: “The player pays.” Otherwise, withdraw them the amount and a separate line: "The owner pays." The last line on the screen should be displayed the phrase: "The game is over."
#
#
#
#Example:
#Bone cube: 3
#Owner's cube: 4
#Sum: 7
#The owner pays
#The game is over


x=int(input('Add number:'))
y=int(input('Add number:'))
if x>=y:
  print(x-y,'\nGamer will pay!\nGame over.')
else:
 print(x+y,'\nOwner will pay.\nGame over.')



# Homework 4.5.7

#What should be done
#
#Vasya gained experience and decided to look for a vacancy with a greater salary. He was attracted by the vacancy with a strange formula for calculating wages:
#
#200*hours/2**3+hours
#
#He wants to understand how many hours you need to work out so that there is enough to repay the loan and food.
#
#Write a program that requests three numbers with the user: the amount of hours worked, the balance of the loan and the amount of money for food. After that, the salary is calculated by the formula. If the salary is more or equal to the amount that is required for a loan and food, then a message is displayed: “There is enough hours. You can relax. " Otherwise: “There is not enough clock. You have to work more! "
#
#Example:
#Enter the spent clock: 80
#Enter the balance on the loan: 1000
#Enter on food: 5000
#There is not enough hours. You have to work more!


hours=int(input('Add hours:'))
food=int(input('Add numbers:'))
kredit=int(input('Add numbers:'))
x=(200*hours)/2**3+hours
y=food+kredit
if x>y:
    print('You can work.')
else:
    print('You need to find another job.')



#  Homework  4.5.8

#What should be done
#
#The user introduces three numbers.
#
#Write a program that displays the maximum of these three numbers on the screen (all numbers are different). Use additional variables if necessary.


a=int(input('Add number:'))
b=int(input('Add number:'))
c=int(input('Add number:'))
print('Maximum is',end=' ')
if b<=a>=c:
    print(a)
elif a<=b>=c:
    print(b)
elif a<=c>=b:
    print(c)
