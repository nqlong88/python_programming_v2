#Class 5 03/23/2020

# for loop
'''for num in range (1,11):'''
'''
# while loop: zero time; onetime or infinitely 
# While <something> true

Problem 1
num = 5

# WHILE LOOP:

while num < 10:
    print ('yeah!!!')
# because number always less than 5 -> keeps printing
   # num -= 1
# now does it keep running?: NO IT KEEPS RUNNING
    num += 1
# ends when reaches 10'''

#Problem 2:
'''
secret = 7 #7 here is an integer
answer = int(input('please pick a number:')) # CONVERT TO INT -> input would be a string when entered via keyboard

while answer != secret:
    answer = int(input('pick again:'))

print ('you are correct!')
'''    


# EXERCISE 3
#check if a string is a palindrome: same fwds as bwds:

# 'level', 'racecar', 'aaaa'

#use while loop

string = 'levela'
first = 0
last = -1
'''
while string[first] == string[last] and first < len(string):
    first +=1
    last += -1

print ('yes')
'''

# reverse string first and then compare: need start from end and add one by one
new_string =''
index = len(string) - 1
while index >= 0:
    new_string += string[index]
    index -= 1

if new_string == string:
    print('it is a palindrome') 
else:
    print('it is not a palindrome')