#Class 4 (3/18/2020)

#EXAMPLE 1
numbers = [8, 5, 17]

#insert the number -5 at the front of the list

numbers.insert(0,-5)

# find number of element
print(len(numbers))

last_el = numbers.pop() 
print(last_el)
print(len(numbers))


#print second element
print(numbers[1])
print(numbers)

#EXAMPLE 2
grades = [70 , 85, 91, 23, 60, 45 , 90, 56, 77, 88]

#add 5 to each grade in the list
# we have access each element / position, change the element
# we need to access to index, we use range
'''
range(len(grades))

for grade in grades:
    print (grade, end=' ') # end= ' ' make it print horizontally
    grade += 5

    

print(grades)'''
# Use: range(len(grades)) -> Loop is the index
for index in range(len(grades)):
    grades [index] += 5
print(grades)

#make each word past tense in this list

#EXAMPLE 3

verbs = ['like', 'hate', 'fake', 'rake']

for word in range(len(verbs)): #range function used to create an index
    verbs[word] += 'd' #    verbs[word] = verbs[word] + 'd' -> can flip to have d in front 

print (verbs)

# Example 4 - Game of Pig
import random
val = random.randint(1, 6)


player1_total = 0
player2_total = 0

turn = 1

#player1's turn
if turn == 1:
    #start a loop until total score = 20
    for player1_total in (0,20):
        if player1_total < 20: #check if max = 20
            score = random.randint(1, 6)
            if score == 1:
                player1_total = 0
                turn = 0
            else: 
                player1_total += score
        else:
            print ('Player 1 wins')
            

    

#player2's turn
if turn == 0:
    score = random.randint(1, 6)
    if score == 1:
        player2_total = 0
        turn = 0
    else: 
        player2_total += score
#check if max = 20
if player1_total == 20:
    print ('Player 2 wins')


'''print(player1_total)
print(player2_total)'''