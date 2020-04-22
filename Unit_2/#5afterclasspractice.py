# March 25, 2020

#1 • Given a string, replace every letter with its position in the alphabet
string = 'abc'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
#index + len

position = 0
new_string = ''
while position < (len(string)):
    new_string += str(alphabet.index(string[position])+1) #NOTE: ALWAYS TEST SIMPLE OUTPUT
    position += 1

print(f' the new string is {new_string}')

'''
print(string[0])
'''


#2 • Given a list of numbers, find the largest number in the list

numbers = [12, 4, 5, 78, 19, 16, 100]

maxnumber = 0

for number in numbers:
    if number > maxnumber:
        maxnumber = number
print (maxnumber)