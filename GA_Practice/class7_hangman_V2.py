# Create hangman program:
# VERSION 2: Create function to solve the duplicate issue

word_bank = ['toronto', 'new york', 'vancouver', 'seatle', 'seoul', 'hanoi'] #['toronto', 'new york', 'vancouver', 'seatle', 'seoul', 'hanoi']

# 1. Set up game: pick from wordbank and setup blank

import random
word = word_bank[random.randint(0,len(word_bank)-1)]
game_progress = []

while len(game_progress)<len(word):
    game_progress += '_'


# 2. Set turns limit & kick-off
limit = len(word)*2
turn = 0

print(f' LET US START: {game_progress}; you have {limit} turns')


#3 Look up function: to look up and put letter in the blank list
def check(guess,word):
    #answer = game_progress
    check_index = 0
    while check_index < len(word): # while loops through all char in word
        if word[check_index] == guess:
            game_progress[check_index] = guess # this line puts the correct guess in answer list
        check_index += 1
    return game_progress


# 4. Kick off & Play: using unfunction in #3
guess = input('TO START: make a guess: ')
turn = turn + 1
while turn <= limit:
    if guess in word:
        print(check(guess,word))
        print(f' remaining turns = {limit - turn}')
        if '_' not in game_progress:
            print('YOU WON!')
        else:
            guess = input('Correct, continue: ')
    else:
        guess = input('Nope, play again: ')
    turn += 1
if '_' in game_progress: # need to condition this to make sure it doesn't show when game won!
     print('GAME OVER!')

