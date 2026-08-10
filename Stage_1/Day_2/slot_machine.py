# ==============================
# SLOT MACHINE GAME CONFIGURATION
# ==============================

# Maximum number of lines that players can bet on
# This controls the highest number of active betting lines in the game
MAX_LINES = 3


# Minimum amount a player can bet
# Prevents zero or negative bets
MIN_BET = 1


# Maximum amount a player can bet per line
# Prevents extremely large bets
MAX_BET = 100





# ==============================
# DEPOSIT SYSTEM
# ==============================

# Function responsible for collecting the player's starting money
# The player must enter a valid positive number
def deposit():

    # Keep asking until the player enters acceptable input
    while True:

        # Ask the player how much money they want to add
        amount = input("How much do you want to deposit: $")


        # Check whether the input contains only numbers
        # Prevents errors when converting text to integer
        if amount.isdigit():

            # Convert the user's input from string to integer
            amount = int(amount)


            # Make sure the deposit is greater than zero
            # A player cannot start with negative or zero money
            if amount > 0:

                # Exit the validation loop when input is correct
                break


            # Handle invalid values like 0
            else:
                print("The amount must be greater than 0")


        # Handle text input like "abc"
        else:
            print("The amount must be a number")


    # Return the valid deposit amount to the main game
    return amount





# ==============================
# BETTING SYSTEM
# ==============================

# Function responsible for asking the player
# how much money they want to risk on each line
def bet():

    # Continue asking until a valid bet is entered
    while True:

        # Ask the player for their bet amount
        stake = input("How much do you bet on each line: $")


        # Ensure the input is numeric
        if stake.isdigit():

            # Convert text input into integer
            stake = int(stake)


            # Ensure the bet is positive
            if stake > 0:

                # Stop asking when the bet is valid
                break


            else:
                print("The stake must be greater than 0")


        else:
            print("The stake must be a number")


    # Return the player's chosen bet amount
    return stake





# ==============================
# BETTING LINES SYSTEM
# ==============================

# Function responsible for deciding how many lines
# the player wants to bet on
#
# Example:
# 1 line  = smaller risk
# 3 lines = higher risk and higher possible reward
def get_lines():

    # Keep requesting input until valid
    while True:

        # Ask player how many lines they want to activate
        lines = input("How many lines would you bet for?: ")


        # Check if the input is a number
        if lines.isdigit():

            # Convert input to integer
            lines = int(lines)


            # Make sure the number of lines is positive
            if lines > 0:

                # Accept the input
                break


            else:
                print("The lines amount must be greater than 0")


        else:
            print("The lines amount must be a number")


    # Return the number of selected betting lines
    return lines





# ==============================
# MAIN GAME CONTROLLER
# ==============================

# Main function controls the overall game flow:
#
# 1. Get player's starting money
# 2. Ask how many lines they want to play
# 3. Ask their bet amount
# 4. Calculate total cost
# 5. Check if they can afford the bet
def main():


    # Get the player's available money
    deposit_amount = deposit()


    # Get the number of lines they want to activate
    lines = get_lines()



    # Keep asking for a bet until it fits the player's balance
    while True:


        # Get the amount they want to bet per line
        stake = bet()



        # Calculate the total money being risked
        #
        # Formula:
        # total bet = amount per line × number of lines
        #
        # Example:
        # $5 per line × 3 lines = $15 total bet
        total_bet = stake * lines



        # Check whether the player has enough money
        if total_bet > deposit_amount:

            # Reject the bet because it exceeds available money
            print("There is not enough money to proceed with this bet")


        # If affordable, continue the game
        else:
            break



    # Show the final betting information
    print(
        f"Your bet is ${stake} on {lines} lines, the total bet is: ${total_bet}"
    )





# Start the slot machine program
# This calls the main controller function
main()