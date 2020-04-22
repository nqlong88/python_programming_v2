# Create hangman program:


# VERSION 1: Can't update list with duplicated letters
# 1. Set up game: pick from wordbank and setup blank
word_bank = ['angle', 'hangman', 'toronto', 'hoaancut']

import random

word = word_bank[random.randint(0,len(word_bank)-1)]
game_progress = []

while len(game_progress)<len(word):
    game_progress += '_'

print(f' LET US START: {game_progress}')

# 2. Set turns limit

limit = len(word)*2
turn = 0

# 3. Kick off & Play: if under limit guess: and update game_progress[index] with the right guess
guess = input('TO START: make a guess: ')
turn = turn + 1
while turn <= limit:
    if guess in word:
        game_progress[word.index(guess)] = guess
        print(game_progress)
        print(f' remaining turns = {limit} - {turn}')
        if '_' not in game_progress:
            print('YOU WON!')
        else:
            guess = input('Correct, continue: ')
    else: 
        if '_' not in game_progress:
            print('YOU WON!')
        else:
            guess = input('Nope, play again: ')
    turn += 1
print('GAME OVER!')

