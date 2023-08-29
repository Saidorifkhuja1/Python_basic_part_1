# Homework 8.6.1

#What should be done
#Your spacecraft crashed on a deserted planet. Food does not grow here, but you saved a 100-kilogram bag of buckwheat from the wreckage. From past experience, you know that if you eat economically, then you will leave four kilograms of buckwheat per month.
#
#To estimate the buckwheat budget, you decided to write a program that will withdraw information about how many kilograms of buckwheat you should have in reserve in a month, two and so on, until it ends. Use the for cycle.

months=int(input('Add months;'))
buckwheat=100
for i in range(1,months+1):
    buckwheat-=4
    print('After',i,'months you mast have',buckwheat,'kg buckwheat ')




## Homework  1.8.2

#What should be done
#The Mirprogbank finally divided law-abiding citizens and debtors and placed them in different bases. But the bank is in no hurry to put pressure on the non -payers. The bank operators were given the task of calling every fifth debtor from the list (numbering starts from scratch) and clarify how much each of them owed the bank.
#
#Write a program that receives data on the number of debtors, and then asks every fifth (starting from scratch) his debt. At the end, the total amount of debts is displayed.
#
#Example 1
#
#Enter the number of debtors: 13
#
#Debtor with number 0
#
#How much should it? 1000
#
#Debtor with number 5
#
#How much should it? 5000
#
#Debtor with number 10
#
#How much should it? 2000
#
#Total debt: 8000
#
#Example 2
#
#Enter the number of debtors: 10
#
#Debtor with number 0
#
#How much should it? 1000
#
#Debtor with number 5
#
#How much should it? 5000
#
#Total debt: 6000

names=int(input('Add amout of debtors:'))
summ=0
for n in range(0,names,5):
    print("Number debtor:",n)
    debt=int(input('Amount of debt:'))
    summ+=debt
print('Amount of all debts',summ)




#homework  1.8.3

#What should be done
#We are developing a micro -oprogram - a reverse countdown timer for microwave furnaces. Some users do not like the squeak of sound.
#
#There is a task to remove the sound according to readiness and replace it with a message on the LED screen. In our case, we will display a message with the back count in the console in seconds from “Reverse_Timer” until the moment of readiness, that is, “0” seconds, and ask the user whether he is ready to take the food.
#
#The user at any time can interrupt the warm -up mode by introducing “1” (that is, reply “Yes, the food is ready”), then the program displays the message “Your food is ready, you can pick up” and shows which second the timer was interrupted.
#
#If the user answers “0”, which is equivalent to “no”, then the timer decreases. When he reaches “0” seconds, we display the message “Your food is ready, carefully hot!”
#
#In this task we use the Forb cycle.
#
#“Reverse_timer” is a variable counter, the value of which is requested from the user through the input entry function.
#
#Set the time to zeroing the timer.
#Use the Forb cycle.
#On each iteration, ask the character the question whether he wants to stop warming up now or not.

time=int(input('Add time:'))
z=time
for n in range(time,0,-1):
   #print(n)
   x=int(input('if you wont to stop add (0) for continue (1):'))
   z-=1
   print('Left',z,'seconds')
   if x!=0:
        continue
   else:
        break
print('Be carefull!')



#Homeworkk 1.8.4

#What should be done
#Write a program that reads three numbers A, B and C from the keyboard, considers and displays the arithmetic mean of all numbers from the segment [A; b], multiple of the number c.
#
#Recommendations
#The Range (Start, Stop) function does not include the Stop border, stops without reaching it.

a=int(input('Enter first number:'))
b=int(input('Enter first second:'))
c=int(input('Enter first third:'))
amount_n=0
summ=0
for n in range(a,b):
    if n%c==0:
        print(n)
        amount_n=amount_n+1
        summ=summ+n
        arifmetic_m=summ/amount_n
print(arifmetic_m)




# Homework 1.8.5

#What should be done
#Before studying the functions from programming, Sasha decided to revive his knowledge about the functions of mathematics. Help Sasha write a program that will consider the value of the function at each point of the segment with the desired step, starting from the end).
#
#Write a program that receives the beginning and end of the segment to the input, as well as a step (negative), and then calculates the function Y at each point of the segment and displays the answer to the screen with the desired step, starting from the end.
#
#The function itself looks like this:
#
#‌y=x**3+2*x**2-4*x+1
#
#Example
#
#Introduce the beginning of the segment: −2
#
#Enter the end of the segment: 2
#
#Enter a step: −1
#
#At point 2, the function is 9
#
#At point 1, the function is 0
#
#At point 0, the function is 1
#
#At point −1 the function is 6
#
#At the point −2 the function is 9
#
#Recommendations
#The Range (Start, Stop) function does not include the Stop border, stops without reaching it.


x=int(input('Add begin of functinon:'))
y=int(input('Add end of functinon:'))
step=int(input('Add step of functinon:'))
function=0
for n in range(y,x-1,step):
     function=n**3+2*(n**2)-4*n+1
     print('In ',n,'function equal to',function)




# Homework 1.8.6

#What should be done
#The student’s monthly scholarship is educational_grant rubles, and accommodation costs exceed the scholarship and amount to expenses rubles a month.
#
#The increase in prices monthly increases costs by 3%, except for the first month. Please note that every month prices increase by 3% of the relative last month.
#
#Make a program for calculating the amount of money that you need to get from your parents once at the beginning of their studies so that you can live a school year (ten months), using only this money and a scholarship.
#
#Example
#
#Enter the scholarship: 10,000
#
#Enter accommodation costs: 12000
#
#A month of expenditure 12,000 is missing 2000
#Month of spending 12360.0 is not enough 4360.0.0
#A month of waste 12730.8 is missing 7090.8
#A month of spending 13112.7 is missing 10203.52
#A month of spending 13506.1 is missing 13709.63
#A month of spending 13911.2 is missing 17620.92
#Month of spending 14328.6 NO is enough 21949.55
#Month of spending 14758.4 lacks 26708.03
#Month of spending 15201.2 lacks 31909.27
#A month of spending 15657.2 is not enough 37566.55
#You need to ask parents 37566.55 rubles


scholarship=int(input('Add scholarship:'))
cost=int(input('add cost:'))
result=cost-scholarship


for n in range(9):
    cost=cost*103/100
    
    result+=cost-scholarship

print(result)

 # Homework 1.8.8
number=int(input('Enter number:'))
s=0

for i in range(1,number+1):
  s+=((-1)**i)*(1/(2**i))
print(s)


x=int(input('Enter number:'))
numerator=1
denominator=1
for n  in range(1,7):
  numerator=numerator*(x-2**n+1)
  denominator=denominator*(x-2**n)
  answer=numerator/denominator
print(answer)


# Homework 1.8.10

#Что нужно сделать
#X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд места в одном ряду. Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.
#
#На вход подаются два числа: количество мальчиков X и количество девочек Y. В ответе выведите какую-нибудь строку, в которой будет ровно X символов B, обозначающих мальчиков, и Y символов G, обозначающих девочек, удовлетворяющую условию задачи. Пробелы между символами выводить не нужно. Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку «Нет решения».
#
#Пример 1
#
#Введите количество мальчиков: 5
#
#Введите количество девочек: 5
#
#Ответ: BGBGBGBGBG
#
#Пример 2
#
#Введите количество мальчиков: 5
#
#Введите количество девочек: 3
#
#Ответ: BGBGBBGB


boys=int(input('Add number of boys:'))
girls=int(input('Add number of girls:'))
answer=' '
if (boys>2*girls)or(girls>2*boys):
    print('Impossible')
elif boys>=girls:
    k=boys-girls
    for bgb in range(k):
        answer+="BGB"
    for bg in range(girls-k):
        answer+='BG'
else:
    k=girls-boys
    for gbg in range(k):
         answear+='GBG'
    for gb in range(boys-k):
        answer+='GB'
print(answer)

