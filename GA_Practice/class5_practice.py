# Practice 1:

# Create a guessing engine:
'''
key = 15
response = int(input('please choose your guess: '))

while response != key:
    response = int(input('please choose again: '))

print('CORRECT')
'''

#practice 2: check # palindrome in a list


#WHILE
my_list =['AAA', 'Baa', 'AA', 'CCC', 'Caa']

palin_count = 0

for item in my_list:
    index = len(item)-1
    new_item =''
    while index >= 0:
        new_item += item[index]
        index -= 1
    if new_item == item:
        palin_count += 1
    
print(f'palindrome count is {palin_count} using While loop')


# FOR:
my_list =['AAA', 'Baa', 'AA', 'CCC', 'Caa']

palin_count = 0

for item in my_list:
    new_item =''
    for char in item:
        new_item = char + new_item
    if new_item == item:
        palin_count += 1
print(f'there are {palin_count} using for loop')

#prob 2 • Given a list of numbers, find the largest number in the list

#Steps:
#1. pop out a value & Create the other list w/o a value:
#2 compare
numbers = [12, 4, 5, 13]

index = 0
larger_than_count = []

while index <= len(numbers)-1:
    number = numbers[index]
    numbers.pop(index)
    new_list = numbers
    for new_item in new_list:
        count = 0
        if new_item < number:
            count += 1
    larger_than_count.append(count)
    index +=1

print(f'test {larger_than_count}')

'''
#test: see how to compare a number of items in a list
numbers = [12, 4, 5, 78, 19, 16]
index = 0
pop_numbers = numbers.pop(index)
print(pop_numbers)
test_number = numbers[index]
count = 0
tracker =[]
for number in pop_numbers:
    if number < test_number:
        count +=1
print (count)
tracker.append(count)
print (tracker)'''
