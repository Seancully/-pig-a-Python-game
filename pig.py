import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4: ")

max_score = 100 # sets max score to 100
player_scores = [0 for _ in range(players)] # array stores player scores

while max(player_scores) < max_score:

    for players_i in range(players): # ensures for one players turn only
        print("\nPlayer {}'s turn!\n".format(players_i+1))
        print("Your total score is {}".format(player_scores[players_i]), "\n") # prints players score (overall)

        current_score = 0 # current score set to 0 as default

        while True: 
            should_roll = input("Would you like to roll? (y/n): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turns done!")
                current_score = 0 # makes sure we dont add score if roll a 1
                break
            else:
                current_score += value
                print("You rolled a {}!".format(value)) # prints roll for current player

            print("Current score: {}".format(current_score)) # prints current score for player

        player_scores[players_i] += current_score # players score for this turn added to players overall score
        print("Player {}: {}".format(players_i+1, player_scores[players_i])) # prints players score (overall)

        if player_scores[players_i] >= max_score:
            print("\nPlayer {} won!".format(players_i+1))
            break




