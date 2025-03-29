
import random

def dice():
    dice = []  
    for i in range(5):  
        dice.append(random.randint(1, 6))  

    score = 0  

    while dice:  
        print("Rolled Dice:", dice)  
        
        min_die = min(dice)  
        score += min_die  
        dice.remove(min_die)  

        print("Kept:", min_die)  
        print("Current Score:", score)  

        if dice:  
            input("Type 'roll' to roll the next dice: ").strip().lower()
            dice = [random.randint(1, 6) for i in range(len(dice))]  
    print("No dice left to roll. Turn ended.")  
    return score  

def game():
    player1_score = 0
    player2_score = 0

    while player1_score < 20 and player2_score < 20:  
        print("\nPlayer 1's turn:")
        round_score = dice()  
        if round_score == 20:  
            print("Player 1 reaches 20! Player 2 wins!")
            
        
        print("\nPlayer 2's turn:")
        round_score = dice()  
        if round_score == 20:  
            print("Player 2 reaches 20! Player 1 wins!")
            

game()