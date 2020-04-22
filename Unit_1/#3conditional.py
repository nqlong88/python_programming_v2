# CLASS 3, 3/16/2020
#truthy vs falsey
# : to start block
'''
if 'hello' and 0:
    print('this is true')
else:
    print('this is not true')
'''


num = 5

if num > 10:
    print('num is greater than 10')
    print ('this is good')


#LECTURE 3: EXERCISE
#count negative reading
readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

count = 0 # Start Count with a value
# needs to create a count variable
for temp in readings:
    if temp < 0:
        count += 1

print (count)

#find average of positive reading

positive_count = 0
positive_sum = 0

for temp in readings:
    if temp > 0:
        positive_count += 1
        positive_sum += temp
        # At this stage both variables has a final value after loop ran
average = positive_sum/positive_count # Needs to set variable after loop here to capture value
print (positive_count)
print(positive_sum)
print(average)

#Problem 2
titles = ['The Avengers', 'Avengers age of Ultron', 'Captain A, The First']

#count how many title has 'The' in it
count = 0
for title in titles:
    if 'The' in title:
        count += 1

print (f'List has {count} title with "The"')


#show how many vowels are in a string

#Problem 3:
string = 'There is a long string that has only a few vowels'
# look: a e i o u
count = 0
vowels = ['a','e','i','o','u'] #Try to simplify
for char in string:
    #for vowel in vowels:
    if char in vowels: #try: if char in (a,e,i,o,u) -> Tuples   
        count += 1
        

print (f'there are {count} vowels in string')





