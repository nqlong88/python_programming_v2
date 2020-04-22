# problem 3

odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar', '123451' , '0.0', 'papa', '-pq-']

''' for loop
find string > 3 (len)
index0 = index(len)'''



count = 0

for string in odd_strings:
    if len(string) > 3 and string[0] == string[len(string)-1]: # need to set equal == and make sure minus 1 to avoide out of range
        count += 1

print (f'there are {count} strings with more than 3 charaters whose the first and last characters are the same')

'''
string = 'teststring'

print(string[len(string)-1])'''

# SOLUTION:
#Note: string[0]  -> index character in a string
#Finding index[-1] -> last character -> and -2 move up
