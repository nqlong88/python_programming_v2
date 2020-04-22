#This attempts to do hw3 prob 3 w/o boolean (TRUE/FALSE):
#2) dictionary checking prob 5 hw3: using .count
legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

#write a letter count function: by creating a dictionary: {'letter' : #count}
def letter_count(word):
    count_dict ={}
    for char in word:
        #use function .get(key, default value in case key missing):
        count_dict[char] = count_dict.get(char,0) + 1 #here .get allows for: 1) set value = 0 vs current blank; 
        #2) iterate and count 
    return count_dict

#start looking thru each word in word list and compare letters vs. allowable list

def possible_words(legal_words,letter_list):
    answer=[]
    for word in legal_words:
        char_count = letter_count(word) 
        for char in word:
            if char_count[char] <= letter_list.count(char):
                answer.append(word) #this will append everytime char_count[char] < letter count
                #need something to append at word level/not char level
    return answer

print(f' result is: {possible_words(legal_words,letters)}' )

