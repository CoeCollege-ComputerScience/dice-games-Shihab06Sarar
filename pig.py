import random

def dice():
    score = 0
    repeat = True
    while repeat:
        roll = random.randint(1, 6)
        print("Roll:", roll)
        if roll == 1:
            score = 0
            print("Score:", score)
            print("Turn over")
            repeat = False
        else:
            score += roll
            print("Score for this turn:", score)
            if input("Roll again? y/n ") == "y":
                repeat = True
            else:
                repeat = False
    return score

def pig():
    player1 = 0
    player2 = 0
    
    while player1 < 100 and player2 < 100:  
        print("Start turn Player 1")
        round_score = dice()
        print ("\n")
        player1 += round_score  
        print("Total score player 1:", player1)
        print ("\n \n")
        if player1 >= 100:
            print("\nPlayer 1 wins!")
            
        print("Start turn Player 2")
        round_score = dice()
        print ("\n")
        player2 += round_score  
        print("Total score player 2:", player2)
        print ("\n \n")
        if player2 >= 100:
            print("Player 2 wins!")
           

pig()
