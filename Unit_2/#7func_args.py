#Class 7: March 30, 2020
#functoon that takes any number of paratmerters
# add any number of numbers

def mult(*args): #Must be exact: "*arg" * does not mean mult. here 
    product = 1 
    for num in args:
        product *= num
    return product

print(mult(1,2,3,4))


#keyword arguments
def message(name, msg='hello:'):
    print(msg + ' ' + name)

message('Long') # dont need to print because print is in function already 
message('Princeton', msg= 'hi')


# func that allows any number of keyword agreemetns 
l = [1,2,3]
for item in l:
    print(item, end= '')


#Group Challenge: HANGMAN PROBLEM

words = ['one', 'twenty', 'hundred']

import random

word_index = random.randint(0,len(words)-1) #random.choice
word = words[word_index]

answer = []

for char in word:
    answer += '_'
print(answer, end= '')

guess = input('please take guess: ')
letter_position = word.find(guess,0,len(word)-1)

if letter_position == -1:
    guess = input('guess again: ')
else:
    answer.replace(guess,letter_position,len(word)-1)

print(answer)
























'''
Donyell:
words = ['one', 'twenty', 'hundred']  
  
word = random.choice(words) 
  
print("Guess the characters") 
  
guesses = '' 
turns = 6

while turns > 0: 

    failed = 0

    for char in word:     
        if char in guesses:  
            print(char)     
        else:  
            print("_") 
            failed += 1
              
    if failed == 0: 

        print("You Win")  
        print("The word is:", word)  
        break
    
    guess = input("Guess a character: ") 
       
    guesses += guess  
    
    turns -= 1
    print("You have", + turns, ' guesses')

    if guess not in word: 
         
        print("Wrong")  
          
        if turns == 0: 
            print("You Lose")
From Me to Donyell Hernandez:  (Privately) 08:22 PM
words = ['one', 'twenty', 'hundred']

import random

word_index = random.randint(0,len(words)-1) #random.choice
word = words[word_index]

answer = []

for char in word:
    answer += '_'
print(answer, end= '')

guess = input('please take guess: ')
letter_position = word.find(guess,0,len(word)-1)

if letter_position == -1:
    guess = input('guess again: ')
else:
    answer.replace(guess,letter_position,len(word)-1)

print(answer)
'''