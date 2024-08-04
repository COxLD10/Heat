import random

def roll():
    min_value = 1
    max_value = 10
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (1-10):")
    if players.isdigit():
        players = int(players)
        if  2 <= players <= 8 :
            break
        else:
            print("Must be between 2-8 players. ")
    else: 
        print("Invalid, try again.")

max_score = 500
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for player_idx in range(players):
        current_score = 0

        while True: 
            should_roll = input("Would you like to roll (Y)? ")
            if should_roll.lower() != "y":
                  break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break

            else:    
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)
            
        players_scores[player_idx] += current_score
        print("Your total score is:", players_scores[player_idx])

    

