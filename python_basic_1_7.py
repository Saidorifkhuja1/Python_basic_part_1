#  Homework  7.6.1

#What should be done
#The bank’s database stores data both debtors and law -abiding citizens. The system assigns its number to each person. We have a random sample of ten numbers. True, sometimes the base is buggy and gives out a number with a negative value. And according to the statistics that our “Mirprogbank” gathered, every second user took a loan and did not pay it on time, that is, he is a debtor.
#
#Write a program that, when entering ten numbers, determines how many of them are simultaneously even and positive.

for num in range(10):
  number = int(input('Введите число: '))
  if number%2==0 and number>0:
    print('Correct number',number)
    print()
  else:
    print('Wrong number')
    print()

#  Homework 7.6.2

#What should be done
#
#The accountant was tired of constantly considering the average annual salary of the company's employees and, in order to make life easier, turned to the programmer.
#
#Write a program that accepts the employee’s salary from the user for each of the 12 months and displays the average salary for the year.

salary_sum = 0
avarage_summ=0
for month in range(1,12+1):
    print('Now month', month,)
    salary = int(input("How much your salary: "))
    salary_sum += salary
    #work_months += 1
    avarage_summ=salary_sum//12
print('Your salary for a year;',salary_sum)
print('Your avarage salary is',avarage_summ)

# homework 7.6.3

#What should be done
#We get closer and closer to serious mathematics. One of the classical tasks is the task of finding a number of numbers. And in the future we will meet with her.
#
#The natural number n. Write a program that finds n! (N-factory).
#
#Record n! means the following:
#
#N! = 1 * 2 * 3 * 4 * 5 * ...
#
#Example:
#
#Enter the number: 5
#
#The number of the number 5 is 120

n=int(input('Add number:'))
result=1
for i in range(n,0,-1):
    result*=i
print('Factorial of',n,'is',result)

# Homework 7.6.4
students=int(input('Add amount of students:'))

summ1=0
summ2=0
summ3=0
for student in range(1,students+1):
    score=int(input('Enter score of student.You can add only 3,4 or 5: '))

    if score==5:
        summ1+=1
    elif score==4:
        summ2+=1
    elif score==3:
        summ3+=1
print('Amount of students who takes 5',summ1)
print('Amount of students who takes 4',summ2)
print('Amount of students who takes 3',summ3)
    

#  Homework 7.6.5
number1=int(input('Enter first number:'))
number2=int(input('Enter first second:'))
amount_n=0
summ=0
for n in range(number1,number2+1):
   if n%3==0:
       print(n)
       summ+=n
       amount_n+=1
       arifmetic_m=summ/amount_n
print(arifmetic_m)

#  homework 7.6.6

for n in range(10,99):
  p=n%10
  z=n//10
  if  n==(p*z)*3:
        print(n)

# Homework 7.6.7

cards=int(input('Amount of cards:'))
summ=0
remanining_sum=0
for card in range(1,cards+1):
    summ+=card
for card in range(cards-1):
    remaincards=int(input('Add number  cards:'))
    summ-=remaincards
print("lost card is",summ)
