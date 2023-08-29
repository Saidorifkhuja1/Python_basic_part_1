

#  Homework 12.6.1

# Write a summa_n function that takes one positive integer N and prints the sum of all numbers from 1 to N inclusive.
#
# An example of the program's operation:
#
# Enter number: 5
#
# I know that the sum of numbers from 1 to 5 is 15


def sumNumber():
    number = int(input('Enter number:'))
    summ=0
    for x in range(1,number+1):
      summ+=x
    print('Sum of number from 1 to',number,'is',summ)

print('Here you can add number.')
sumNumber()



#  Homework 12.6.2

# Евгений проходит специальный тест по программированию. Всё шло хорошо, пока герой не наткнулся на тему «Функции». Задание звучит так:
#
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода. Это вызов функции test(). В ней запрашивается на ввод целое число. Если оно положительное, то вызывается функция positive(), тело которой содержит команду вывода на экран слова «Положительное». Если число отрицательное, то вызывается функция negative(), её тело содержит выражение вывода на экран слова «Отрицательное».
#
# Помогите Евгению и реализуйте такую программу.




def positive():
    if x>0:
        print('Positive')

def negative():
    if x<0:
        print('Negative')

def test():
 if x>0:
        positive()
 else:
        negative()

print('Enter number(number!=0):')
x=int(input('>>>'))
test()

# Homework  12.6.3


# Stepan uses a calculator to calculate the sum and difference of numbers, but at work he needs more than just simple arithmetic. He does not want to do anything manually, so he decided to slightly expand the functionality of the calculator.
#
# Write a program that asks the user for a number and the action to be taken with the number: print the sum of its digits, the maximum or minimum digit. Write each action as a separate function, and loop the main program.
#
# The requested numbers must be passed to the sum, maximum, and minimum functions using arguments.

def sumN():
    num = int(input('Enter number:'))
    num_sum = 0
    while num != 0:
        num_sum = num_sum + num % 10
        num = num // 10
    print(num_sum)

def maxN():
    a=int(input('Enter number:'))
    m=a%10
    a=a//10
    while a>0:
       if a%10>m:
          m = a % 10
       a=a//10
    print('the biggerst number is',m)

    
def minN():
  a=int(input('Enter number:'))
  minim=10
  while a:
    d=a%10
    if d<minim:
        minim=d
    a//=10
  print(minim)
    

def calculation():
    text = input("if you wont to find sum numbers     enter 'sum'"
                 "\nif you wont to find maximal       numbers enter 'max'"
                 "\nif you wont to find minimal       number enter 'min':>>")
    if text == 'sum':
        sumN()
    elif text == 'max':
        maxN()
    elif text == 'min':
        minN()


calculation()

# Homework 12.6.4

# A sequence of numbers ending in zero is entered. Implement a function that takes each number as an argument, reverses it, and prints it to the screen.
#
# Example:
#
# Enter number: 1234
# Reverse number: 4321
# Enter number: 1000
# Reverse number: 0001
# Enter number: 0
# Program completed!
#
# Optional: Make sure that numbers are output with leading zeros.
#
# Example:
#
# Enter number: 1230
# Reverse number: 321
#
# The zero we removed is called the leading zero.


def reserveNumber():
  n1=int(input('Enter number:'))
  n2=0
  while n1>0:
        digital=n1%10
        n1//=10
        n2=n2*10+digital
  print(n2)

print('Enter number which you wont to reserve:')
reserveNumber()


# Homework 12.6.5

# We continue to develop a new text editor. This time we were assigned to write a code for it that counts how many times any selected letter or number occurs in the text (and not just the letters Y, as before).
#
# Write a count_letters() function that takes a text as input and counts the number of K digits and N letters in it. The function should display information about the found letters and digits in a certain format.
#
# Example:
#
# Enter text: 100 years in the afternoon
# What number are we looking for? 0
# What letter are we looking for? L
#
# Number of digits 0: 2
# Number of letters L: 1

def findletter():
    text=input('Enter text:')
    firstN=(input('Enter number:'))
    letter=(input('Enter letter:'))
    countL=0
    countN=0
    for symbol in text:
        if symbol==firstN :
            countN+=1
        if symbol==letter:
            countL+=1
    print('Amount of letters:',countL)
    print('Amount of number:',countN)

print("Program for find numbers and letters.")
findletter()




   #Homewoek   12.6.8


# Write a function that calculates the greatest common divisor of two numbers.
def gcd():
    a=int(input('Eter number:'))
    b=int(input('Eter number:'))
    while a!=0 and b!=0:
       if a>b:
            a=a%b
       else:
            b=b%a
    print('Greatesr common devider',a+b)

print('Program for finding common devider. ')
gcd()

# Homework  12.6.9

# What should be done
# You came to work in a game development company, the target audience is children and their parents. A previous programmer had an assignment to make two games in one application so that the user could choose one of them. However, the programmer you took over, before leaving, did not have time to complete this task and left only a small project template. Use this template to implement Rock, Paper, Scissors and Guess the Number games.
#
# Rules of the game "Rock, paper, scissors": the program asks the user for a string and displays whether he won or lost. Rock beats scissors, scissors cut paper, paper cuts rock.
#
# Rules of the game "Guess the number": the program asks the user for a number until he guesses the guess.


import random

def rock_paper_scissors():
    from random import randint
    # moves for the player
    moves = ["rock", "paper", "scissors"]
    while True:
        computer = moves[randint(0,2)]
        player = input("\nrock, paper or scissors? (quit) :").lower()
        if player == "quit":
              print("The game has ended.")
              mainMenu()
              break

        elif player == computer:
              print("Tie!")
        elif player == "rock":
            if computer == "paper":
              print("YoU lose!", computer, "beats", player)
            else:
              print("YoU win!", player, "beats", computer)
        elif player == "paper":
            if computer == "scissors":
              print("You lose!", computer, "beats", player)
            else:
              print("You win!", player, "beats", computer)
        elif player == "scissors":
            if computer == "rock":
              print("You lose!", computer, "beats", player)
            else:
              print("You win!", player, "beats", computer)

def guess_the_number():
    number = random.randrange(1,100)
    guess =int(input("\nGuess a number between 1 and 50."
                     "\nIf you wont to bsck main menu enter-77.>> "))
    while guess != number:
        if guess==77:
            mainMenu()
        elif guess < number:
            print("You need to guess higher. Try again")
            guess=int(input("\nGuess a number between 1 and 50."
                            "\nIf you wont to bsck main menu enter-77.>>   "))
        else:
            print("You need to guess lower. Try again")
            guess = int(input("\nGuess a number between 1 and 50."
                              "\nIf you wont to bsck main menu enter-77.>>  "))
            print("You guessed the number correctly!")





def mainMenu():
    print('\nHere you can chose games')
    game=input('If you wont to play (rock paper scissors) enter "rock"'
               '\nif you wont to plas (guess the number) enter "number">> ')
    if game=='rock':
        rock_paper_scissors()
    elif game=='number':
        guess_the_number()

mainMenu()
