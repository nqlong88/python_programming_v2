# dict comprehension:
#create a new dict w key = letter; value = letter count
string = 'i am a string how many letters do i have'
# .count function
dictionary = {letter : string.count(letter) for letter in string} # use count not get
print(dictionary)

#.get function

string_other = 'iamanotherstring'

def create_dict(string):
    dictionary = {}
    for letter in string:
        dictionary[letter] = dictionary.get(letter,0)+1 #this .get set default value for key = 0
print(dictionary)
    

