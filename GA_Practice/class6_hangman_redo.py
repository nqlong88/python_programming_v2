# create a random word list and kickstart game:

# create and randomize list
word_bank = ['hi', 'sad', 'joy', 'blue']

import random
word = word_bank[random.randint(0, len(word_bank))]

# Start game:

limit = len(word)
progress = []

for char in word:
    progress += '_'

print (f'let us play, here is the word: {progress}, you have {limit} attempts')


# Play:
turn = 0
guess = input('please make your first guess:')
turn = 1

while turn <= limit:
    if guess in word:
        char_index = 0
        while char_index < len(word):
            if word[char_index] == guess:
                progress[char_index] = guess
            char_index += 1
        print (progress)
        print(f' remaining turn {limit - turn}')
        if '_' in progress:
            guess = input('correct, keep going: ')
        else:
            print('you won!')
    else:
        print (progress)
        print(f' remaining turn {limit - turn}')
        guess = input('sorry, pick again: ')
    turn += 1
if turn > limit and '_' in progress:
    print('you lost!')


