# score: a between 80-100; b between 70-80; c between 60-70; F
# randomly generate score

import random

score = random.randint(0,100)

if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'FAIL'
print(f'your score is {score} corresponding to letter grade: {grade}')


#fizzbuzz
#for the first 50 integers
#if divisible by 3, print fizz
# if divisible by 5, print buzz
# if divisible by 15, print fizzbuzz

'''increment = range(1,50)'''
number = 0
for number in range(1,51): #---> USE RANGE FUNCTION HERE 
    #number += 1
    if number % 15 == 0:
        print ('fizzbuzz')
    elif number % 5 == 0:
        print ('buzz')
    elif number % 3 == 0:
        print ('fizz')
    else:
        print(number)
        
        
# find the sum of even numbers between 1 and 10
sumtotal = 0
for number in range (1,10):
    if number % 2 == 0:
        sumtotal += number

print (f'the sum of even numbers is {sumtotal}')
