#Class 6 (03/25/2020)

'''def add_two():
    result = 5 + 5
    print(result)

#call the function: type f name
add_two()'''

#passing arguments to function:

'''
def add_two(a,b):
    result = a + b
    print(result)

add_two(3, 4)
'''

#return a value: 1. Ask to return and 2. Print
def add_two(a,b):
    result = a + b
    return result #return: function stops and return value

print(add_two(3, 4))

#write a function that returns the sum of the integers in a List:

def sum_list(a_list):
    result = 0
    for num in a_list:
        result += num
    return result

values = [1,2,1,515,9]
answer = sum_list(values)

print(answer)


#write a function that reverse a string

def rev_string(my_string):
    new_string = ''
    char = len(my_string)-1 #make sure to substract 1 (since 1st position = index 0)
    while char  >= 0:
        new_string += my_string[char]
        char -= 1
    return new_string

print (rev_string('imastring'))


# The above can also be used w for loop
'''
    for char in range(0,len(my_string)):
        new_string += my_string[char]
        char -= 1
    return new_string'''

#write fucntion find intersections of two list:

def int_list (list_1,list_2):
    common_char = []
    for char_list_1 in list_1:
        if char_list_1 in list_2: # use in list to check in var in list
            common_char.append(char_list_1) # Use append here to add to list
    return common_char

print(int_list([1,2,3,6],[3,4,5,6]))


