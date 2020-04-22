#Model game of pig

player1_total = 0
player2_total = 0

import random
turn = random.randint(0,1)
score = 0 

# player 1 plays if turn = 1
if turn == 1:
    # will build in roll,hold later here
    score = random.randint(1,6) #needs = not == as we assign value here not testing
    if score == 1:
        player1_total = 0
    else:
        player1_total += score
else:
    score = random.randint(1,6)
    if score == 1:
        player2_total = 0
    else:
        player2_total += score


print('player 1 turn, score, total:', turn, score, player1_total, end= "")

print(' / player 2 turn, score, total:', turn, score, player2_total)



#EXAMPLE 2
grades = [70 , 85, 91, 23, 60, 45 , 90, 56, 77, 88]

#add 5 to each grade in the list
# we have access each element / position, change the element
# we need to access to index, we use range

#print(grades[0])

for position in range(0,len(grades)):
    #originally:
    '''Used this code: grades[position]+5 -> this added to that but not yet replace the grade list'''
    grades[position] = grades[position]+5 # this Updated the EXISTING VALUE

print(grades)