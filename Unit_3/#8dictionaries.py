#Class 8

import json

#Dictionary below: format dictionary = [ {'Key' : 'Value'}, ....]
cars = [
    {
        'make': 'Toyota',
        'model': 'Camry',
        'year': '2017',
        'color': 'black'
    },
    {
        'make': 'Toyota',
        'model': 'Prius',
        'year': '205',
        'color': 'white'
    },
    {
        'make': 'Mercedes Benz',
        'model': 'A 250',
        'year': '2019',
        'color': 'grey'
    },
    {
        'make': 'Hyundai',
        'model': 'Elantra',
        'year': '2007',
        'color': 'grey'
    },
    {
        'make': 'Lexus',
        'model': 'IS 300',
        'year': '2020',
        'color': 'blue'
    },
]

#add price:
price = [100 , 200 , 300 , 400 , 500]
'''
index = 0

for car in cars:
    car['price'] = price[index] # NOte that we look at individual item (car) in in dictionary (cars)
    index +=1
'''
# ENUMERATE:
for index, car in enumerate(cars): #returns a pair of index and item in the list / string -> AUTOMATE index
    car['price'] = price[index]

print(json.dumps(cars, indent = 2))


#reverse lookup

state_capitals = {
    'alaska' : 'juneau',
    'colorado': 'denver',
    'texas' : 'austin'
}

capital = 'austin'
answer =''

def reverse_lookup(my_dictionary,value):
    for state in state_capitals:
        if state_capitals[state] == capital: # remember: Interation is over KEY
            answer = f' the state is: {state}' # can also just return state here
        else:
            answer = 'n/a'
    return answer

print(reverse_lookup(state_capitals,capital))


# write a function called frequency_counter, input = a string: 
# return a dictionary w each word and the number of times each word appears 

string = 'this is a string is it it is'

def frequency_counter(sentence):
    keys = sentence.split(' ') #Use split to turn string into list
    dictionary = {}

    for key in keys:
        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1
    return dictionary

print(frequency_counter(string))

#remove duplicate from a list: can create KEYS or use SET