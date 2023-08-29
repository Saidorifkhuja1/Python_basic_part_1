
#    Homework 5.6.1

#What should be done
#In his free time, Vasya loves to play computer games. Once he had a cool idea for the plot of the game. To bring it to life, he began to study the game design. He began to create a game with the protagonist and his pumping system.
#
#Write a program that determines the character level in the computer game. The user introduces the number of "experience points", and the program calculates the level. A new level is given when reaching 1000, 2500 and 5000 “experience points”. The initial level is equal to one.
#
#Example:
#Enter the amount of experience: 6000
#Your level: 4
#
#Example 2:
#Enter the amount of experience: 2000
#Your level: 2
#
#Tips and recommendations
#If possible, pay attention to the reduction of the code. Try not to check the conditions that have already been checked: if you checked the Condition condition, you should not check the Not Condition.

score=int(input('Add score:'))
if  score<1000:
    print('Your level :1')
elif 1000<=score and score<2500:
    print('Your level:2 ')
elif score>=2500 and score<5000:
    print('Your level :3')
elif score>=5000:
    print('Your level :4')



#   Homework 5.6.2
#
#The mathematics teacher invents individual functions to each student that needs to be displayed on the schedule and count. The teacher also understands programming, and in order not to manually consider these functions, he wrote a program that does work for him.
#
#y= {x −12, x>0, 5,  x=0 x2,  x<0
#
#Write a program that receives the number X from the user and calculates the value of function Y according to the following scheme:
#
#
#Recall how it works:
#for x> 0, y = x - 12
#for x = 0, y = 5
#for x <0, y = x2
#
#Example:
#Enter X: 0
#Igrek is 5
#Example 2:
#Enter X: −6
#Igrek is 36
#
#Tips and recommendations
#If possible, pay attention to the reduction of the code. Avoid checking the conditions that have already been checked: if you checked the Condition condition, you should not check the Not Condition.
#


x=int(input('Add number:'))
if x>0:
    y=x-12
    print(y)
elif x<0:
    y=x*2
    print(y)
else:
    y=5
    print(y)



#  Homework 5.6.3

#What should be done
#The university at the Faculty of Cybernetics is a very serious competition - only the strongest, the first ten people from the list come. Then, among those who arrived, it is determined who will receive a scholarship. For a scholarship, the total score must be at least 290 upon admission.
#
#Write a program that receives a student’s place in the list and its score to the input, and then withdraws appropriate reports about the receipt and receipt of the scholarship.
#
#Example 1:
#Enter the place in the list of applicants: 3
#Enter the number of points for exams: 295
#Congratulations, you acted!
#A scholarship will be accrued to you with a bonus.
#
#Example 2:
#Enter the place in the list of applicants: 3
#Enter the number of points for exams: 270
#Congratulations, you acted!
#But you did not have enough points for a scholarship.
#
#Example 3:
#Enter the place in the list of applicants: 11
#Unfortunately, you did not do it.

list=int(input("Add  list number:"))
if list<=10 :
     score=int(input('Add score:'))
     if score>=290:
      print("You passed:")
      print('You will receive a scholarship')
     elif score<290:
       print("You passed:")
       print('But you did not have enough points for the scholarship')
if list>10:
   print('You failed')





#  Homework 5.6.4
#
#The papa programmer was so embroidered that instead of asking his son what assessment he received at school, he wrote the program:
#
#rating = int ('What got in mathematics?'))
#if rating == 2:
#  print ('Bad. Marting to study!')
#if rating == 3:
#  print ('Bad. Marting to study!')
#if rating == 4:
#  print ('Well done! You can relax.')
#if rating == 5:
#  print ('Well done! You can relax.')
#
#
#
#The son looked at the program code and realized that it could be improved. He even told dad how to do this, for which he received the boundless respect of his father.
#
#Copy the program to the editor and optimize:
#
#With a poor assessment (2 or 3), the message is displayed: “Bad. March to study! "
#With a good assessment (4 or 5), the message is displayed: “Well done! You can relax. "
#The program should not have repeated lines.


ratint=int(input('Add number:'))
if  ratinf<4:
    print('Bad.Go to study ')
else:
    print('Good.You can rest')

 #  Homework 5.6.5
x=int(input('Add number:'))
y=int(input('Add number:'))
z=int(input('Add number:'))
if x==y==z:
   print(3)
elif x==y or x==z or y==z:
    print(2)
elif x!=y!=z:
    print(0)


#  Homework  5.6.6

#What should be done
#A family of three people was tired of crowding in odnushka and finally decided to move. When discussing which apartment to buy, based on preferences and the family budget, they settled on two versions:
#
#Choosing an apartment is more spacious (at least 100 m2), but worth no more than 10 million.
#A little expand the search circle, that is, choose a smaller apartment (from 80 m2), but also worth not more than 7 million.
#Write a program that receives the cost of the apartment and its area and displays the message, whether it is suitable.


area=int(input('Add area:'))
cash=int(input('Add cash:'))
if area>=100 and cash<=10000000:
    print('You can buy it.')
elif area>=80 and cash<=7000000:
    print('You can buy it.')
else:
    print('You can not buy it.')




#   Hmework 5.6.7

#What should be done
#Vasya was inspired by the film “Twenty One” and decided to study the mathematics of slot machines. To analyze the data, he needs information about how often three or two identical pictures fall in the machine. To collect data, you need a program that checks this equality.
#
#Three whole numbers are given. Determine how many coinciding among them. The program should display one of the numbers: 3 (if everyone matches), 2 (if two coincide) or 0 (if all numbers are different).
#
#Tips and recommendations
#If possible, pay attention to the reduction of the code. Avoid checking the conditions that have already been checked: if you checked the Condition condition, you should not check the Not Condition.


hour=int(input('Add hour:'))
x=hour
if  (x>=8 and x<10) or (x>=12 and x<14) or (x>=15 and x<18) or (x>=20 and x<22): 

    print('You can receive a parcel')
else: 
    print('You can not receive a parcel')



if (x>=0 and x<8) or (x>=10 and x<12) or (x>=14 and x<15 ) or (x>=18 and x<20) or (x>=22 and x<=24):
    print('You can not receive a parcel')
else:
   print('You can receive a parcel')

