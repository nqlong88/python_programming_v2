'''
Class 10 (April 8, 2020)
	- Review classes
	- List and Dictionary Comprehension
	- Modules
    - File input and output
'''

# A. list comprehension:

nums = [1, 3 , 4 , 6 , 7, 11 , -15 , 28]

#create a list of only even numbers

''' OLD METHOD:
even_nums = []

for num in nums:
	if num % 2 == 0:
		even_nums.append(num)
print(even_nums)
'''

#use a list comprehension:
#even_nums = [num for num in nums if num % 2 == 0] # this is a list comprehension: to create new list from existing

even_nums = [num for num in nums if num %2 == 0 ]
'''
1. start empty ([])
2. start loop inside empty list (for loop)
3. put in the result (num in front for loop)
4. put in condition after for loop (if: ) 
'''
print(even_nums)

vals = [2, 4, 6, 8]

vals_square =[val*val for val in vals] # no if statement require here
print(vals_square)

#create a new list with words longer than 4 characters


words = ['run', 'cat', 'hassle', 'print', 'class', 'pyth']

greater_four = [word.upper() for word in words if len(word) > 4 ] # use word.upper(): to capitalize all chars

print(greater_four)


# B. dictionary comprehesion:

person = {'name' : 'Alice' , 'address' : 'Toronto', 'occupation' : 'Engineer'}

new_person ={person[key] : key  for key in person }
# Alternative: new_person = {key:val for key,val in person.items()}

print(new_person)

colors = {'red' : 'bold' , 'green' : 'lively', 'blue': 'calm', 'yellow' : 'warm'}
#create a new dict w colors whose value either warm or lively

new_color = {key : colors[key] for key in colors if 'Lively' in colors[key] or 'warm' in colors[key]}
print(new_color)


# create a new dict w count of each letter in a string 
'''
def letter_count(word):
    count = {}
    for l in word:
        count[l] = count.get(l, 0) + 1
    return count
'''

'''
string = 'iamateststring'

string_dict = {char : string[count] for char in string count += 1 }
#string_dict = { count for char in string count[char] = count.get(char,0) + 1 }

print(string_dict)
'''

'''
Abdul:
'''
string = 'string'
dict_word = {letter:string.count(letter) for letter in string}
print (dict_word)

