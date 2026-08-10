# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================

# Import random because the computer needs to make unpredictable choices
# The computer should not always choose the same option
import random





# ==============================
# GAME STATE SETUP
# ==============================

# Store the current score of the human player
# Starts at zero because nobody has won yet
user_score = 0


# Store the current score of the computer player
# This keeps track of how many rounds the computer wins
computer_score = 0



# List containing all valid moves available in the game
# The user and computer can only choose from these options
game_options = [
    "rock",
    "paper",
    "scissors"
]





# ==============================
# MAIN GAME LOOP
# ==============================

# Keep the game running continuously
# The loop only stops when the player chooses to quit
while True:


    # Ask the user to choose an option
    #
    # .lower() converts the input to lowercase
    # This makes "Rock", "ROCK", and "rock" work the same way
    user_guess = input(
        "Choose Rock/Paper/Scissors or Q to quit: "
    ).lower()



    # Exit condition:
    # If the user enters "q", end the game loop
    if user_guess == "q":
        break



    # Input validation:
    # Check whether the user's choice exists in the allowed options
    #
    # If the choice is invalid:
    # - Ignore it
    # - Restart the loop
    # - Ask again
    if user_guess not in game_options:
        continue





    # ==============================
    # COMPUTER DECISION
    # ==============================


    # Generate a random number between 0 and 2
    #
    # These numbers represent indexes:
    #
    # 0 → rock
    # 1 → paper
    # 2 → scissors
    random_int = random.randint(0, 2)



    # Use the random index to select the computer's move
    computer_guess = game_options[random_int]



    # Display the computer's choice
    print("computer picked: " + computer_guess)





    # ==============================
    # WINNING LOGIC
    # ==============================


    # Check every possible situation where the user wins
    #
    # Rock beats scissors
    # Paper beats rock
    # Scissors beats paper
    if (
        user_guess == "rock"
        and computer_guess == "scissors"
    ):

        print("You won!")

        # Increase user's score by one
        user_score += 1



    elif (
        user_guess == "paper"
        and computer_guess == "rock"
    ):

        print("You won!")

        # Increase user's score by one
        user_score += 1



    elif (
        user_guess == "scissors"
        and computer_guess == "paper"
    ):

        print("You won!")

        # Increase user's score by one
        user_score += 1



    # If none of the winning conditions happened,
    # the computer wins the round
    #
    # Note:
    # This also counts ties as computer wins in the current version
    else:

        print("You lose the game")

        # Increase computer's score
        computer_score += 1





# ==============================
# FINAL RESULTS
# ==============================


# When the player quits,
# display the final scoreboard
print(f"user scored {user_score}")

print(f"computer scored {computer_score}")


# Friendly closing message
print("Thanks for playing the game")