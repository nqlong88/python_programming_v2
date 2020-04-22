# problem 1:Create a file called dict_functions.py. Write the functions for problems 1 and 2 inside this file.

dict1 = {'a': 1, 'b': 2, 'c':50 }
dict2 = {'w': 'x', 'b': 'y', 'c':'laugh'}

def dict_merge (dict1, dict2):
    new_dict = {}
    for key in dict1:
        if key in dict2:
            if dict1[key] == dict2[key]:
                new_dict[key] = dict1 [key]
            else:
                new_dict[key] = [dict1[key], dict2[key]]
    for key in dict2:
        if key not in dict1:
            new_dict[key] = dict2[key]
    return new_dict

print(f' problem 1: {dict_merge(dict1, dict2)}')

# problem 2: list_to_dict that accepts a person list (which is a list of lists), and returns a
#dictionary. Each list in the person list has only two items. The keys of your result dictionary should be the
#first item in each list, and the value should be the second item.
        
name = ['name', 'alice']
job = ['job', 'enginneer']
city = ['city', 'toronto']

def list_to_dict(list1, list2, list3):
    person = {}
    person[list1[0]] = list1[1]
    person[list2[0]] = list2[1]
    person[list3[0]] = list3[1]
    return person

print(f' prob 2: {list_to_dict(name, job, city)}')


# problem 3: reverse_dict to reverse a dictionary. This means, given a dictionary, return a new
#dictionary that has the keys of as values, and the values as keys
''' NEED TO COMPLETE'''

dictionary = {'a': 1, 'b': 1} # how to convert lists to tuples

def reverse_dict(dictionary):
    rev_dictornary = {}
    for key in dictionary:
        rev_dictornary[dictionary[key]] = key
    return rev_dictornary

print (f' prob 3: {reverse_dict(dictionary)}')

'''
dictionary = {'a': 1, 'b': [2,3,4]} # how to convert lists to tuples
count = 0
for key in dictionary:
    if '[' in dictionary[key]:
        count += 1
        
print(count)
'''


