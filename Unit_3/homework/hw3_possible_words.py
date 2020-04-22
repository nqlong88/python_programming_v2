#possible_words that accespts a list of words and a list of characters, and returns
#the valid words that can be made from the characters given.\\

legal_words = ['go', 'bat' 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

'''
approach will be to create a dictionary that tallies all letters w count from list of words
i.e.: all_char_dict
{
    'a' : 3
    'b' : 4
    'c': 5
}

then looking at letters: create a similar list
i.e.: avail_char_dict

and optimize: by drawing down
'''


'''
def possible_words(legal_words,letters):
    # which words in the word list can be formed from 
    # char list

    # look at each work in word list 
    for word in legal_words:
        for char in word:
            if char in letters:

'''

