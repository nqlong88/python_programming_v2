#Problem 1:
#Write a function called letter_count that takes a string and a single character, and returns the number of
#times that character appears in the string.

letter = 'a'
string = 'i am a sample string'


def letter_count(string,letter):
    index = 0
    common_letter = 0
    while index < len(string)-1:
        if string[index] == letter:
            common_letter += 1
        index += 1
    return f' Prob 1: letter {letter} appears: {common_letter} times'

print(letter_count(string,letter))


#problem 2:Write a function called count_words that takes a string and returns the number of words in the string.

string2 = 'let me know how many words are in this string'
space = ' '

def word_count(string,space):
    index = 0
    count = 0
    while index <= len(string2) - 1:
        if string[index] == space:
            count += 1
        index += 1
    return f' Prob 2: word count: {count+1}'

print(word_count(string2, space))

#problem 3: reverse_list that takes a list and returns a new list with the items reversed.

org_list = ['mean', 'median', 'max']

def rev_list(org_list):
    index = len(org_list) - 1
    new_list = [ ]
    while index >= 0:
        new_list.append(org_list[index])
        index -= 1
    return f' prob 3: the reversed list is {new_list}'

print (rev_list(org_list))


#problem 4: that takes a list of integers and an integer (called the pivot), and returns
#a list containing two lists:
#• one with all the numbers less than the pivot
#• the other with all the numbers greater than or equal to the pivot

integers = [102,20,13,4,55,62]
pivot = 40

def split(integers):
    index = 0
    smaller_list = []
    larger_list = []
    while index <= len(integers) - 1:
        if integers[index] < pivot:
            smaller_list.append(integers[index])
        else:
            larger_list.append(integers[index])
        index += 1
    return f' prob 4: Pivot = {pivot}: smaller list: {smaller_list} / larger list: {larger_list}'

print (split(integers))

#problem 5: is_isogram that takes a string and returns true if all the characters are unique (no repeated characters), or returns false otherwise.

string  = 'computer'

def is_isogram(string):
    index_1 = 0
    index_2 = index_1 + 1
    check = []
    while index_1 <= len(string) -1:
        while index_2 <= len(string) -1:
            if string[index_1] == string[index_2]:
                check.append('False')
            index_2 += 1
        index_1 += 1
    if 'False' in check:
        result = 'False'
    else:
        result = 'True'
    return f' prob 5: Are all characters unique?: {result}'

print(is_isogram(string))


#problem 2: Using split method

#prob 5: Solutions (in class)

#Version 1:
def is_isogram2(a_string):
    seen_before = []
    for char in a_string:
        if char in seen_before:
            return False
        else:
            seen_before.append(char)    
    return True

print(is_isogram2('long nguyen'))

#Version 2:
    # Solve using Prob 1: Letter count function. If count > 1 -> FALSE


#Version 3: using FIND function
def is_isogram3(string):
    current_index = 0
    while current_index <= len(string)-2:
        if string.find(string[current_index], current_index+1, len(string)-2) != -1:
            return False
        current_index += 1
    return True

string.find()

