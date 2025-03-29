
import random

def roll_dice():
    input("Type 'roll' to roll the dice:...") 
    dice = [random.randint(1, 6) for _ in range(10)]  
    print(f"Rolled Dice: {dice}")
    return dice

def game():
    players = ["Player 1", "Player 2", "Player 3"]
    
    while len(players) > 1:  
        for player in list(players):  
            print(f"\n{player}'s turn:")
            target = random.randint(1, 6) 
            print(f"{player} predicts: {target}")
            
            dice = roll_dice() 
            
            if dice.count(target) < 2:  
                print(f"{player} couldn't find a pair! {player} is out of the game.")
                players.remove(player)  
            else:
                print(f"{player} found a pair and stays in the game!")

    print(f"\n{players[0]} is the last player remaining and wins the game!")

game()
