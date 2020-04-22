import random
def play_pig():
    player1_score, player2_score = 0, 0
    turn = random.randint(0, 1)
    #while either player has not reached a score of 10
    while(True):
        #if its player 1s turn roll or hold
        if turn == 0:
            choice = input('[PLAYER 1] Roll or hold:')
            if choice == 'r':
                round_score = random.randint(1, 6)
                if round_score == 1: #player looses turn and score gets set to 0
                    player1_score = 0
                    turn = 1
                else:
                    player1_score += round_score
                print('round score {}, total score {}'.format(round_score, player1_score)) 
            else:
                turn = 1
        if turn == 1:
            choice = input('[PLAYER 2] Roll or hold: ')
            if choice == 'r':
                round_score = random.randint(1, 6)
                if round_score == 1: #player looses turn and score gets set to 0
                    player2_score = 0
                    turn = 0
                else:
                    player2_score += round_score
                print('round score {}, total score {}'.format(round_score, player2_score))
            else:
                turn = 0
        #check if a player has won
        if player1_score >= 20 or player2_score >= 20:
            break
    #print the player who won the game
    if player1_score >= 10:
        print('PLAYER 1 WINS!!!')
    else:
        print('PLAYER 2 WINS!!!')
play_pig()