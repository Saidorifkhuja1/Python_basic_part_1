

# Homework 13.6.1

# Last time the teacher wrote a program that outputs numbers in floating point format, but he remembered that he did not take into account one important thing: numbers can go from zero.
#
# Given a positive number x (x > 0). Your task is to convert it to floating point format, i.e. x = a * 10^b, where 1 ≤ a < 10. Note that x is now greater than zero, not greater than one. Provide input control.
#
# Example 1:
#
# Enter number: 92345
#
# Floating point format: x = 9.2345 * 10 ** 4
#
# Example 2:
#
# Enter number: 0.0012
#
# Floating point format: x = 1.2 * 10 ** -3

def big_num(num):
  step = 0
  final_num = num
  while num > 10:
    num //= 10
    step += 1
  print('floating point format: x =', final_num * 10 ** -step, '* 10 **', step )
  


def small_num(num):
  step = 0
  final_num = num
  while num < 1:
    num *= 10
    step += 1
  print('floating point format: x =', final_num * 10 ** step, '* 10 **', -step )


num = float(input('Enter number: '))
if num > 1:
  big_num(num)
elif num < 1:
  small_num(num)
else:
  print('Input Error. The number must be greater than zero')




# Homework 13.6.2

# Yura writes various useful functions for Python to make it easier for other programmers to work. He wanted to write a function that would find the maximum of the listed numbers. He already has a function for finding the maximum of two numbers. Yura thought: maybe it can be somehow used to find the maximum already from three numbers?
#
# Help Yura write a program that finds the maximum of three numbers. To do this, use only the function of finding the maximum of two numbers.
#
# As a result, the program should implement two functions:
#
# maximum_of_two - the function takes two numbers and returns one (the largest of the two);
# maximum_of_three - the function takes three numbers and returns one (the largest of three); however, it must use the first maximum_of_two function for comparisons.


def func_biggest(num_1,num_2):
  bigger = ((num_1 + num_2) + abs(num_1 - num_2)) / 2
  return bigger



num_1 = int(input("Enter first number: "))
num_2 = int(input('Enter second number: '))
num_3 = int(input("Enter third number: "))

first_bigger = int(func_biggest(num_1,num_2))
maximum =int(( first_bigger + num_3 + abs(first_bigger - num_3)) / 2)

print(maximum, ' - biggest number.')


# Homework 13.6.3

# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет каждое число на число, которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова переворачивает и выводит ответ на экран.
#
# Пример:
#
# Введите первое число: 102
# Введите второе число: 123
#
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
#
# Сумма наоборот: 225


def reverse(number):
  rev_number = ''
  while number != 0:
    rev_number += str(number % 10)
    number //= 10
  return int(rev_number)


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
rev_num_1 = reverse(num_1)
rev_num_2 = reverse(num_2)

summ_num = rev_num_1 + rev_num_2
print("\nfirst number reserve: ", rev_num_1)
print("second number reserve: ", rev_num_2, '\n')
print('summ: ', summ_num)
print('summ reserve:', reverse(summ_num))



# Homework 13.6.6

# It is known that the amplitude of a swinging pendulum decays each time by 8.4% of the amplitude of the previous swing. If you swing a pendulum, then, strictly speaking, it will never stop, just the amplitude will constantly decrease until we consider such a pendulum to have stopped. Write a program to determine how many times the pendulum will swing before we think it stops.
#
# The program receives as input the initial amplitude of oscillation in centimeters and the final amplitude of oscillation, which is considered to be the stop of the pendulum. Provide input control.
#
# Example:
#
# Enter initial amplitude: 1
#
# Enter stop amplitude: 0.1
#
# The pendulum is considered to have stopped after 27 oscillations
def func_action(start, stop):
  action = 0
  while start > stop:
    start = (start - (start * 8.4 / 100))
    action += 1
  return action


start = float(input('Enter start Amplitude: '))
stop = float(input("Enter stop amplitude: "))

if start < 0 or stop < 0:
  print("enter a positive number")
elif start < stop:
  print("The pendulum is already considered to have stopped")
else:
  print("The pendulum is considered to have stopped after", func_action(start, stop), "hesitation")



# Homework 13.6.7


def func_danger(max_level):
  max_level = float(max_level)
  min_x = 0
  max_x = 4
  danger = ((max_x ** 3) - (3 * (max_x ** 2)) - (12 * max_x) + 10)
  while abs(danger) - max_level > 1e-15:
    middle = (min_x + max_x) / 2
    danger = ((middle ** 3) - (3 * (middle ** 2)) - (12 * middle) + 10)
    
    if danger < 0:
      max_x = middle
    if danger > 0:
      min_x = middle
   
  print("Approximate depth of safe masonry: ", middle)
      



def isfloat(max_level):
  try:
    float(max_level)
    return True
  except ValueError:
    return False



max_level = input("Enter the maximum acceptable level of danger: ")

#print(isfloat(max_level))

if isfloat(max_level):
  func_danger(max_level)
else:
  print("Error")


# Homework 13.6.8

def func_factorial(number):
  factorial = 1
  for step in range(1, number + 1):
    factorial *= step
  return factorial

def func_range(range_factor, x):
  start = 1
  for action in range(range_factor):
    start *= x
  return start

def func_minus(number):
  minus = -1
  for action in range(number + 1):
    minus *= -1
  return minus
               
              

start = 1
range_factor = 2
answer = 1

x = int(input("Enter х: "))
precizion = float(input("Enter precision "))

while (func_range(range_factor, x) / func_factorial(range_factor)) >= precizion:

  answer += (func_minus(start)) * (func_range(range_factor, x)/ func_factorial(range_factor))
  range_factor += 2
  start += 1
print (answer)



# Homework 13.6.9


def func_pay(years, percent, credit):
  nominator = (percent * ((1 + percent) ** years))
  denominator = ((1 + percent ) ** years) - 1
  coef = nominator / denominator
  pay = coef * credit
  return pay
  
def func_order_after_three_years(all_credit):
  pay = round(func_pay(years, percent, all_credit), 2)
  for period in range (1, 4):
    all_credit -= (pay - (all_credit * percent))
  return all_credit
      
def func_first_three_years(all_credit):
  pay = round(func_pay(years, percent, all_credit), 2)
  for period in range (1, 4):
    print("\nPeriod: ", period)
    print('\n\nBalance of debt at the beginning of the period:', all_credit)
    print('Paid percentage: ', all_credit * percent)
    print('paid body credit: ', pay - (all_credit * percent))
    all_credit -= (pay - (all_credit * percent))
    if period == 3:
      print ('\n\nBalance of debt at the beginning of the period:', all_credit)
      print('=' * 50)

def func_balanse(new_years, new_percent, new_credit):
 
  pay = round(func_pay(new_years, new_percent, new_credit), 2)
  for period in range (1, new_years + 1):
      print("\nperiod: ", period)
      print('\n\nBalance of debt at the beginning of the period:', new_credit)
      print('Paid percentage: ', (new_credit * new_percent))
      print('paid body credit: ', pay - (new_credit * new_percent))
      new_credit -= (pay - (new_credit * new_percent))
      if period == new_years:
        print('\nLeft debt: ', new_credit)


all_credit = float(input('Enter su credit: '))
years = int(input('For how many years given? '))
percent = int(input('What percentage per year? '))
percent = percent / 100

func_first_three_years(all_credit)


new_years = int(input('\nFor how many years is the contract extended? '))
new_percent = float(input('Increasing the rate to: '))
new_credit = float(func_order_after_three_years(all_credit))

new_years += (years - 3)
new_percent = new_percent / 100

func_balanse(new_years, new_percent, new_credit)




