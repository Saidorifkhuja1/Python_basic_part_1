#  Homework 6.7.1

#What should be done
#One evening, the nephew came home to Vasya and complained about the difficulties with mathematics lessons: he could not deal with the degrees of numbers. Vasya decided to help the nephew and write a program that will clearly see the construction of numbers to a third degree.
#
#Write a program that builds to a third degree each number from 1 to N and displays the result on the screen.

number=int(input('Add Numbers:'))
while number>0:
    print(number**3)
    number-=1




#  Homework 6.7.2

#What should be done
#Write a robot for collectors. At the very beginning, he asks the name of the debtor and the amount of the debt, and then begins to demand from him repayment until the debtor enters the right amount (equal to the amount of the debt or more). After repayment of the debt, the robot reports this to the user and thanks him.
#
#Example
#Vasily, your debt is 100 rubles.
#How many rubles will you make right now to repay it? 50
#Little, Vasily. Let's do it again.
#How many rubles will you make right now to repay it? 90
#Little, Vasily. Let's do it again.
#How many rubles will you make right now to repay it? 110
#Great, Vasily! You have paid off the debt. Thank you!
#
#Recommendation
#Please note: count the amount of funds deposited, this does not correspond to the condition of the problem.

name=input('Add name:')
debt=int(input('Add debt:'))
cash=int(input('Add cash:'))
while debt!=cash:
     print('Come on',name,"one more time:")
     cash=int(input('Pay again:'))
     if debt==cash:
        break
print('Thank you')





#  Homework 6.7.3

#What should be done
#The unsuccessful accountant again goes awry: they bring him such large accounts that the numbers are not placed on paper.
#
#Write a program that would consider for him how many numbers in the introduced number. Please note that the number 0 has one digit.

number=int(input('Add number:'))
digits=0
num=number
while num>0:
    digits+=1
    num=int(num/10)
print('There are',digits,'digitts in',number)





#Homework 6.7.4

#Vasya posted its new application on the platform for beginner developers, users can assess the application: from −100 to 100. He wanted to compare the number of positive and negative reviews, for this he in advance all the reviews so that at the end there were those that are those that are those that are those that were equal to zero.
#
#Write a program that finds the number of positive and the number of negative numbers in the sequence. The sequence ends in number 0.
#
#Example
#Enter the number: −4
#Enter the number: −90
#Enter the number: 6
#Enter the number: 0
#Number of positive numbers: 1
#Number of negative numbers: 2


number='Add number:'
number+='(If you wont to stop add (0)) '
value= ' '
positive=0
negative=0
while True:
     value=int(input(number))
     if value>0:
         positive+=1
     elif value<0:
            
        negative+=1
     elif value==0:
            break
     
print('Thank you')
print('Amount of positives',positive)
print('Amount of negatives',negative)




# Homework 6.7.5

#What should be done
#Maxim programs all day at work and goes home in the evening. Every hour, the authorities throw him several tasks that need to be solved until the next working hour. In addition, every hour the wife calls Maxim. He knows that if he picks up the phone, his wife will ask to go to the store in the evening.
#
#Write a program in which it is considered how many tasks Maxim performed in a day (eight hours). If he picked up the phone at least once, then at the end additionally withdraw the message: "You need to go to the store."
#
#Example
#
#An eight -hour working day began.
#
#1st hour
#
#How many tasks will Maxim solve? 1
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 0
#
#2nd hour
#
#How many tasks will Maxim solve? 2
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 0
#
#3rd hour
#
#How many tasks will Maxim solve? 3
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 0
#
#4th hour
#
#How many tasks will Maxim solve? 4
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 1
#
#5th hour
#
#How many tasks will Maxim solve? 5
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 0
#
#6th hour
#
#How many tasks will Maxim solve? 1
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 0
#
#7th hour
#
#How many tasks will Maxim solve? 2
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 1
#
#8th hour
#
#How many tasks will Maxim solve? 3
#
#The wife calls. Answer the phone? (1 - yes, 0 - no): 0
#
#The working day is over. Total tasks: 21
#
#You need to go to the store.


print('Working day started.')
work_h=int(input('Enter work hours:'))
tasks=int(input('Amount of tasks which you need to do :'))
calls=()
calls_c=0
tasks_c=0
hours=0
while hours<work_h:
    hours+=1
    print(hours,"-hours")
    task=int(input('How many taskes did you do :'))
    tasks_c+=task
    calls=int(input('Wife colled,did you answear?(1-yes,0-no):'))
    calls_c+=calls
print('Working day end.Amount of tasks which you did:',tasks_c)
if calls_c>0:
   print('You need to go shop:')



#   Homework 6.7.6

#The deposit of the bank is X rubles. It increases annually by P percent, after which the fractional part of the cents is discarded. Determine how many years the contribution will be at least y rubles.
#
#Write a program that, according to the numbers x, y, p, determines how many years will pass before the amount reaches the value of Y

deposite=int(input('Enter deposite:'))
summ=int(input('Summa which you wont:'))
percent=int(input('Percentage for year:'))
summ2=()
year=0
while summ>deposite:
    summ2=(deposite/100)*percent
    deposite+=summ2
    year+=1

print('You need to wait',year,'years')


#  Homework 6.7.7

#In one of the practical works, we did the task where the papa programmer wrote a program for his son, which asks him to guess the number. The drawback of the program was that the poor son had to restart it every time to guess the number. Now that we know much more, it's time to fix this drawback and at the same time improve the game itself a little.
#
#Write the to-game program that requests the number until he guesses him. Display messages in accordance with an example.
#Example (made a number 7)
#
#Enter the number: 3
#
#The number is less than necessary. Try again!
#
#Enter the number: 10
#
#The number is more than necessary. Try again!
#
#Enter the number: 8
#
#The number is more than necessary. Try again!
#
#Enter the number: 7
#
#You guessed! The number of attempts: 4


while True:
      number = int(input('Add number:'))
      if number<9:
        print('Wrong number, tray again please:')
        print('Higher than',number)
      elif number>9:
        print('Wrong number, tray again please:')
        print('lower than',number)
      elif number==9:
           break

print('Good deal')
 



# Homework 6.7.8

#What should be done
#Change the boy and the computer from the past task in places. Now the boy makes the number between 1 and 100 (inclusive). The computer can ask the boy: “Your number is equal, less or more than the number n?”, Where n is the number that the computer wants to check. The boy answers one of the three numbers: 1 - equal, 2 - more, 3 - less.
#
#Write a program that, using a chain of such questions and answers, the boy guesses the number.
#
#Additionally: make so that you can guaranteed to guess the number for seven attempts.
#
#Clue
#
#If desired, find a description of the binary search algorithm and try to apply in this task. The analysis of such a solution will be in the next module.


x=int(input('Enter number:'))
maximum=100
temporareliy=1
attempts=0
half=50
while True:
    attempts+=1
    print(half)
    
  
    print('Your number equal,higher or lower number',half,'?')
    answer=int(input('1-equal,2-higher,3-lower:'))
    if answer==2:
      temporareliy=half
      half=((temporareliy+maximum)//2)
    elif answer==3:
       maximum=half
       half=((temporareliy+maximum)//2)
    else:
      break
print('I found')
print('I found in ',attempts,'-attempts')

