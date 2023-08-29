# Homework 10.6.1
size=int(input('Enter number:'))
size2=int(input('Enter number:'))
for row in range(size+1):
    for col in range(0,size2+1,2):
        print(row+col,end='\t')
    print()

# Homework 10.6.2

n= int(input("Enter number: "))
for start in range(n+1,):
   for number in range(start):
        print(start, end=' \t')
   print()


# Homework 10.6.3
x_lim=int(input('Enter number of first syde:'))
y_lim=int(input('Enter number of second syde:'))

for y in range(y_lim):
    for x in range(x_lim):
        if y == 0 or y==y_lim-1:
            print('-', end='')
        elif x == 0 or x == x_lim - 1:
            print('|', end='')
        elif y==0 or y==y_lim+1:
            print('-', end='')
        else:
            print(' ', end='')
    print()


# Homework 10.6.4


for x in range(10):
    for y in range(10):
        if x==y:
            print('^',end=' ')
        elif x==-y+9:
            print('^', end=' ')
        else:
            print(' ', end=' ')
    print()



# Homework 10.6.5
n=int(input('Amount of numbers:'))
count=0

for number in range(n):
    number=int(input('Enter number:'))
    x=True
    for i in range(2,number):
        if number%i==0: 
          x=False
          break 
    if x:
          count+=1
print('Amount of prime numbers',count)


# Homework 10.6.6

n=int(input('Enter number:'))
fact=1
summ_f=0
for x in range(1,n+1):
    fact=fact*x
    summ_f+=fact
    
print(summ_f)

#  Homework 10.6.7

num_q=int(input('Enter amount of number:'))
summ=0
for number in range(1,num_q+1):
    num_sum=0
    num=int(input('Enter  number:'))
    compare_num=num
    while num!=0:
        num_sum=num_sum+num%10
        num=num//10
        if summ<num_sum:
            summ=num_sum
            search_num=compare_num
            
print('The largest number by the sum of digits:',search_num,'the sum of its digits',summ)



#      Homework 10.6.8
high=int(input('Enter high of piramida:'))
count=0
for row in range(0,high*2,2):
    print(' '*(high-count),end='')

    for col in range(row+1):
        print('#',end='')
    print()
    count+=1

#  Homework 10.6.9
high=int(input('Enter high of piramida:'))
count=0
number=1
for row in range(0,high+1):
    print(' '*(high-count),end='')
    count+=1
    for col in range(1,row+1):
        print('',number,end='')
        number+=2
    print()

# Homework 10.6.10
depth=int(input('Enter depth of pit:'))
for line in range(depth):
    for left_number in range(depth,depth-line-1,-1):
        print(left_number,end='')
    point_count=2*(depth-line-1)
    print('.'*point_count,end='')
    for right_number in range(depth-line,depth+1):
        print(right_number,end='')
    print()

