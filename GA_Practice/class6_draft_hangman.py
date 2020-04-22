# index character
word = 'one'

print(word.index('e'))


# replace

string = ['a', 'b', 'c']

string[2] = 'haha'

print(string)


#hangman:

hangman = ['_', '_', '_']

word2 = 'onnex'
guess = 'n'

if guess in word2:
    hangman[word2.index(guess)] = guess
    print('yes guess in word')

print(word2.index(guess))
print(hangman)

#hangman: find char in word function (incl duplicative):
word3 = 'onnexox'
guess = 'o'

def check(guess,word):
    answer = []
    while len(answer)<len(word3):
        answer += "_"
    check = 0
    while check < len(word3):
        if word3[check] == guess:
            answer[check] = guess
        check += 1
    return answer

print (check(guess,word3))


