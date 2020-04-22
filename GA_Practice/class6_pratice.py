#Practice 1: Create a sum function: for numbers in list

#1: using FOR loop

def sum_list(numbers):
    sum_total = 0
    for num in numbers:
        sum_total += num
    return sum_total

input_list = [1, 3, 6, 7, 9]

print(f' the sum total FOR is: {sum_list(input_list)}')


#2: using WHILE loop
def sum_listWHILE(numbers):
    sum_total = 0
    num = 0
    while num <= len(numbers)-1:
        sum_total += numbers[num]
        num += 1
    return sum_total

input_list2 = [1, 3, 6, 7, 100]

print(f' the sum total WHILE is: {sum_listWHILE(input_list2)}')

# Practice 2:
#write a function that reverses a string:
# 1. create a new empty string as shell
# 2. start picking charater to assemble
# 3. loop thru all characters
# 4. output

#WHILE LOOP

def rev_a_string(string):
    new_string =''
    index = len(string) - 1
    while index >= 0:
        new_string +=  string[index] #made mistake here either += new value or old = old + new
        index -= 1
    return new_string

input_string = 'abcdef'
print(rev_a_string(input_string))

#FOR LOOP:

def rev_string_forloop(string):
    new_forloop_string =''
    string_check =''
    for letter in string:
        new_forloop_string = letter+new_forloop_string 
    if new_forloop_string == forloop_string:
        string_check = string_check + 'strings are the same'
    else:
        string_check =  string_check + 'strings are NOT the same'
    return f'Reverse string is: {new_forloop_string}; and {string_check}'
    

forloop_string = 'apple computer'
print(rev_string_forloop(forloop_string))


# practice 3: write a function to check # palindrome in a list

my_list =['AAA', 'Baa', 'AA', 'CCC', 'Caa']

def count_palindrome(sample_list):
    count = 0 #Made mistake and had count in the for loop: count needs to be started before the loop. Otherwise it will always be 0
    for string in sample_list:
        index = len(string)-1
        new_string =''
        # Had count = 0 here before: wrong -> this reset count to 0 everytime
        while index >= 0:
            new_string += string[index]
            index -= 1
        if new_string == string:
            count += 1
    return f' the count is {count}' 

print(count_palindrome(my_list))


'''
string = 'aavaaab'
index = len(string)-1
new_string =''
count = 0
while index >= 0:
    new_string += string[index]
    index -= 1
if new_string == string:
    print ('same SHIT')
'''

#write fucntion find intersections of two list:

#use FOR
list_1 = ['a', 'b', 'c', 'd']
list_2 = ['a', 'b', 'x', 'y']

def common_item (list_1, list_2):
    count = 0
    for item in list_1:
        if item in list_2:
            count += 1
    return f'Using FOR, the number of common items is: {count}'

print(common_item(list_1,list_2))

#use WHILE

list_1 = ['a', 'b', 'c', 'd']
list_2 = ['a', 'b', 'x', 'y']

def common_itemwhile (list_1, list_2):
    count = 0
    index = 0
    while index <= len(list_1)-1:
        if list_1[index] in list_2:
            count +=1
        index +=1 #note that here: index is not in the If
    return f'Using WHILE, the number of common items is : {count}'

print(common_itemwhile(list_1,list_2))