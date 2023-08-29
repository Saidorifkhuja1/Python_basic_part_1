

# Homework 9.6.1

# The old captain needs to replenish the team, but only the worthy will get on the ship! He selected ten people. Those who shout the word "Caramba" will get on board.
#
# What should be done
# The user enters ten words. Write a program that determines how many of them match the word "Caramba".

firsr_s=(input('Enter first symbol of word:'))
word_c=0
for word in range(10):
   word=(input('Enter 10 words:'))
   if word==firsr_s :
     word_c+=1
     print('Amount of similar word:',word_c)

# Homework 9.6.3

# There is a messenger in which sometimes there are problems when sending messages: they get an extra character - an asterisk. Users got tired of it, so they began to leave for other services. But one of them was interested in what positions an asterisk usually appears in. To find out, the user needs to prepare strings in which the "*" character occurs exactly once.
#
# What should be done
# Write a program that determines the ordinal number of an asterisk in a string.
#
# Example:
#
# Enter the text: "Hello how are you."
#
# The symbol "*" is in position 3.

text=input('Enter text:')
symbol_s=input('Enter symbol which you are searching:')
symbol_c=0
for symbol in text:
    symbol_c+=1
    if symbol==symbol_s:

        break
print('Symbol',symbol_s,'is in',symbol_c,'position')


#   Homework 9.6.4

# The city plans to build an open-air theater, but first you need to estimate how many rows to make, the seats in them and what should be the distance between the rows.
#
# What should be done
# Write a program that takes as input the number of rows, seats, and free meters between the rows, and then displays a rough theater layout on the screen.


# Enter number of rows: 5
# Enter number of seats in a row: 7
# Enter the number of meters between rows: 3
# Scene
#
#    ======= *** =======
#    ======= *** =======
#    ======= *** =======
#    ======= *** =======
#    ======= *** =======
#


ranks=int(input('Amount of ranks:'))
seats=int(input('Amount of seats:'))
meters=int(input('Amount of seats:'))
for n in range(ranks):
 print('='*seats,"*"*meters,'='*seats)


##  Homework 9.6.5

# A "colleague" Billy was sent to Valli's robot. This is its first landing on Mars, so it is tested in a rectangular room measuring 15 × 20 m. The rover lands in the center of the room (at points 8, 10), then control is transferred to the operator, that is, the user of your program.
#
# The program asks in which direction the operator wants to point the robot: north (W key), south (S key), west (A key), or east (D key). The operator makes a choice, the rover moves one meter in that direction, and the program reports the new position of the robot. If the rover hits a wall, it should not try to move towards the wall - in this case, its position does not change.
#
# What should be done
# Create a program to control Billy the robot.
#
# Example:
#
# [Program]: The rover is at position 6, 19, enter the command:
#
# [Operator]: A
#
# [Program]: The rover is at position 5, 19, enter the command:
#
# [Operator]: W
#
# [Program]: The rover is at position 5, 20, enter the command:
#
# [Operator]: W
#
# [Program]: The rover is at position 5, 20, enter the command:


x=10
y=8
while (x>0) and (y>0) and (x<=20) and (y<=15):
  print('Mosrsoxod is staying positiom',x,y)
  order=input('Enter order:')
  
  if order=='W':
      y+=1
      if y==15:
        print('\nYou are infromt of wall!!')
  elif order=="S":
      y-=1
      
  elif order=='A':
      x-=1
      if x==20:
        print('\nYou are infromt of wall!!')
  elif order=='D':
        x+=1


# Homework 9.6.6





text=input('ENter text:')
lenth=0
count=0
for symbol in text:
    if symbol=="s":
       count+=1
    elif count>lenth:
        lenth=count
    else:
        count=0
print(lenth)

# Homework 9.6.7

text=input('ENter text:')
lenth=0
count=0
for symbol in text:
    if symbol!=" ":
        count+=1
    else:
        if count>lenth:
          lenth=count
          count=0
print(lenth)
