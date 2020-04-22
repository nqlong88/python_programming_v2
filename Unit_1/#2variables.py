car_total = 12

#check if car total is even
if car_total % 2 == 0:
    print('car total is even')
else:
    print('car total is odd')


#using elif with multiple conditions
score = 51
if score >= 80:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'C'
else:
    grade = 'D'

print(grade)


#fizzbuzz
#for the first 50 integers

#if divisible by 3, print fizz
# if divisible by 5, print buzz
# if divisible by 15, print fizzbuzz


for loop in range(1, 51):
    # need to initiate a loop here by creating variable and add sequencing 
    number = 0 + loop
    #trick here is to start with 15 first (which is the most stringent requirement: combo of 3 and 5)
    if number % 15 == 0:
        print('fizzbuzz')
    elif number % 5 == 0:
        print('buzz')
    elif number % 3 == 0:
        print('fizz')
    else:
        print (number)


#SOLUTION: don't need to create new loop
for num in range(1, 51):
    if num % 15 == 0:
        print ('fizzbuzz')
    elif num % 5 == 0:
        print ('buzz')
    elif num % 3 == 0:
        print ('fizz')
    else:
        print (num)


# find the sum of even numbers between 1 and 10
# here we need to have a sum to begin. Then: start a loop
total = 0
for num in range (1, 11):
    if num % 2 ==0:
       # total = total + num #calculate running sum.
       #Beter way: "+=" for running sum
       total += num 
  
print (total)

#LECTURE 3 (03/16/2020)
#Review: if score 80-100 Print A; 
#Option 1: Print DIRECTLY
#Option 2: Assign VARIABLE

Finalgrade = 50
if Finalgrade > 80:
    print ('A')
    # or can assign new variables: Lettergrade = 'A'
elif Finalgrade > 60:
    print ('B')
else: 
    print ('C')


