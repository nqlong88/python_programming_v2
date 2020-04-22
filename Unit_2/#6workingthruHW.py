#1 • Given a string, replace every letter with its position in the alphabet
string = 'Abc'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
#index + len

new_string =' '
#use lower case to convert: string.lower():


for char in string.lower():
    #check where letter is in the alphabet: dont forget to add 1
    position = alphabet.index(char)

    #need to add to new string: Covert to string
    new_string += str(position+1)

print(new_string)
