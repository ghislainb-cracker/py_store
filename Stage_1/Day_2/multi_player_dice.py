# Import the random library because the game needs randomness
# The dice roll result should not be predictable, so we use Python's built-in random generator
import random


# Function responsible for simulating one dice roll
# It generates and returns a random number between 1 and 6
# This keeps the dice logic separated from the main game logic
def roll_dice():

    # Define the possible minimum and maximum values of a normal dice
    min_score = 1
    max_score = 6

    # Generate a random integer inside the dice range
    # Example: could return 1, 2, 3, 4, 5, or 6
    rolled_number = random.randint(min_score, max_score)

    # Send the dice result back to wherever the function was called
    return rolled_number



# Ask the user how many players want to participate
# The game only supports between 2 and 4 players
while True:

    # Get player count as text input because all input from users is initially a string
    players = input("How many players (2-4): ")


    # Check whether the input contains only numbers
    # This prevents errors when converting text like "abc" into an integer
    if players.isdigit():

        # Convert the valid numeric input from string to integer
        players = int(players)


        # Validate that the number of players follows the game rules
        # If valid, stop asking and continue with the game
        if 2 <= players <= 4:
            break

        # If the number is outside the allowed range, ask again
        else:
            print("Only between 2 and 4 players are allowed")


    # Handle cases where the user entered something that is not a number
    else:
        print("Enter a valid number")



# Define the score needed to win the game
# The first player who reaches this score wins
max_score = 50


# Create a list to store every player's total score
# Each player starts with 0 points
#
# Example:
# If there are 3 players:
# users_scoring = [0, 0, 0]
users_scoring = [0 for _ in range(players)]


# Display the initial scores of all players
print(users_scoring)



# Main game loop
# Continue running the game until at least one player reaches the winning score
while True:
    while max(users_scoring) < max_score:


    # Give every player a turn in order
    # range(players) creates indexes like:
    # 0 -> Player 1
    # 1 -> Player 2
    # 2 -> Player 3
        for player_idx in range(players):


        # Announce whose turn it is
            print(f"Player {player_idx + 1}, it is your turn")


        # Store points earned only during this specific turn
        # This resets every time a player starts a new turn
            current_score = 0



        # Keep asking the player if they want to continue rolling
        # The player can roll multiple times in one turn
            while True:


            # Ask whether the player wants another dice roll
                user_input = input("Do you want to roll the dice (y): ").lower()


            # If the player chooses anything except "y",
            # their turn ends and they keep their accumulated points
                if user_input != "y":
                    break



            # Call the dice function to generate a random dice value
                value = roll_dice()


            # Show the result of the dice roll
                print(f"You rolled: {value}")



            # Losing condition:
            # Rolling a 1 means the player loses all points earned in this round
            # Their total score from previous rounds is not affected
                if value == 1:

                # Reset only the current turn score
                    current_score = 0

                    print(
                        f"You rolled a 1, so your round score is now {current_score}"
                    )

                # End this player's turn immediately
                    break



            # If the dice value is not 1:
            # Add the dice value to the temporary round score
                else:
                    current_score += value

                    print(f"Your current round score is {current_score}")



        # After the player finishes their turn:
        # Add the points earned this round to their permanent total score
            users_scoring[player_idx] += current_score


        # Display all players' updated scores
            print(f"Your total score is: {users_scoring}")