#Hw3 Review: 1) Check type prob 3 & 2) word checking prob 5 

#1) check type: rev dict i value being string -> turn to key
sample_dict = {
    'a':[1,2,3],
    'b': [4,5,6]
}

new_dict ={}
for key in sample_dict:
    if type(sample_dict[key]) is list: #check type of data type(data) is ...
        new_dict[tuple(sample_dict[key])] = key #convert to tuple: tuple(data)
    else:
        new_dict[sample_dict[key]] = key

print(new_dict)


#2) dictionary checking prob 5 hw3: using .count
legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
'''
#for each word in list: 
1. count letter: compare each letter in word to letter list
2. if letter < letters ok
'''
# understand the get function for use with dictionaries:
'''
test_dict = {
    'a': 4,
    'b' : 6
}

test = test_dict.get('a',5)
print(f' testing .get function {test}')
'''

#write a letter count function: by creating a dictionary: {'letter' : #count}
def letter_count(word):
    count_dict ={}
    for char in word:
        #use function .get(key, default value in case key missing):
        count_dict[char] = count_dict.get(char,0) + 1 #here .get allows for: 1) set value = 0; 2) iterate and count 
    return count_dict

#start looking thru each word in word list and compare letters vs. allowable list

def possible_words(legal_words,letter_list):
    answer=[]
    for word in legal_words:
        valid_word = True #WHY DO WE NEED THIS?
        char_count = letter_count(word) #need to setup a new var and bring function in: this creates dicts for words
        for char in word:
            if char_count[char] > letter_list.count(char): # Use char_count: new dict from applying letter_count function above
                valid_word = False # Need this to single out those that are not valid (w/o this): append directly does not work
                #if we flip sign to > valid_word = False & do a separate if valid_word: append, it would work
                # I think python can only catch the instance it's False; so need to mark it once loops thru this instance: otherwise it's not registed?
        if valid_word:
            answer.append(word)
    return answer

print(f' result is: {possible_words(legal_words,letters)}' )



'''
#Revised Solution below:
def possible_words(word_list, char_list):
    #which words in word_list can be formed from the 
    #charaters in char_list
    valid_words = []
    #iterate over word_list
    for word in word_list:
        is_word_valid = True # True is a boolean variable
        #get a count of each character in word
        char_count = letter_count(word)
        #check each character in the word
        for letter in word:
                if char_list.count(letter) < char_count[letter]: #replace logic (not in and != with <)
                    is_word_valid = False
        #add valid word to a list
        if is_word_valid:
            valid_words.append(word)
    return valid_words

print(possible_words(legal_words,letters))
'''