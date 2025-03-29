import random

def dice():
    input("Type 'roll' to roll the next dice:")  
    dice = []  
    for i in range(3):  
        dice.append(random.randint(1, 6))
    
    total = sum(dice) 
    print(f"Rolled Dice: {dice}, Total: {total}")
    return total

def game():
    player1_wins = 0
    player2_wins = 0
    player1_turn = True  

    while player1_wins < 6 and player2_wins < 6:  
        if player1_turn:
            print("Player 1 is rolling now.")
            roll_total = dice()  
            print ("\n")
            guess = input("Player 2, guess Over or Under: ").strip().lower()  
            # print ("\n")
            print("\nPlayer 2 is rolling now.")
            second_roll_total = dice() 
            
            if (guess == "over" and second_roll_total > roll_total) or (guess == "under" and second_roll_total < roll_total):
                print("\nPlayer 2 guessed correctly! Player 2 wins this round.")
                player2_wins += 1
            else:
                print("\nPlayer 2 guessed wrong! Player 1 wins this round.")
                player1_wins += 1

        else:
            print("\nPlayer 2 is rolling now.")
            roll_total = dice()  
            guess = input("Player 1, guess Over or Under: ").strip().lower()  
            print("\nPlayer 1 is rolling now.")
            second_roll_total = dice() 
            
            if (guess == "over" and second_roll_total > roll_total) or (guess == "under" and second_roll_total < roll_total):
                print("\nPlayer 1 guessed correctly! Player 1 wins this round.")
                player1_wins += 1
            else:
                print("\nPlayer 1 guessed wrong! Player 2 wins this round.")
                player2_wins += 1
        
        print(f"\nScore -> Player 1: {player1_wins}, Player 2: {player2_wins}")
        player1_turn = not player1_turn 
        print("\nSwitching roles...\n")

    if player1_wins == 6:
        print("\nPlayer 1 wins the match!")
    else:
        print("\nPlayer 2 wins the match!")

game()
