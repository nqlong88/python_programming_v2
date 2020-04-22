# Example 4 - Game of Pig
import random
val = random.randint(1, 6)


player1_total = 0
player2_total = 0

turn = 1

#player1's turn
if turn == 1:
    score = 6 #random.randint(1, 6)
    if score == 1:
        player1_total = 0
        turn = 0
    else: 
        player1_total += score

#player2's turn
if turn == 0:
    score = 1 #random.randint(1, 6)
    if score == 1:
        player2_total = 0
        turn = 0
    else: 
        player2_total += score

print(player1_total)
print(player2_total)
