import random

# Ask the user for the highest number the game should allow
last_range = input("Enter the final range number: ")

# Check if the input is a whole number
if last_range.isdigit():
    # Convert the text input into an integer
    last_range = int(last_range)

    # Make sure the range is greater than zero
    if last_range <= 0:
        print("Please enter numbers greater than zero")
        quit()

    # Pick a random secret number inside the chosen range
    random_num = random.randint(0, last_range)
    print("The computer has chosen a number. Try to guess it!")

    # Ask the player for their first guess
    guess = int(input("Enter a guess: "))

    # Keep asking until the player finds the correct number
    while guess != random_num:
        # Give the player a hint based on the guess
        if guess < random_num:
            print("Wrong guess, try again. Your guess is too low.")
        else:
            print("Wrong guess, try again. Your guess is too high.")

        # Ask for another guess
        guess = int(input("Enter a guess: "))

    # Print a success message when the correct guess is made
    print("Correct guess!")
else:
    # If the user types something that is not a number, stop the game
    print("Please enter a valid number")
    quit()
