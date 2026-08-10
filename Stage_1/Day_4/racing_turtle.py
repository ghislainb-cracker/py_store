# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================

# Import turtle because it provides graphics and allows us
# to create moving objects on the screen
import turtle


# Import time because we need to pause the program
# after displaying the winner before closing
import time


# Import random because each turtle needs unpredictable movement
# to simulate a real race
import random





# ==============================
# GAME CONFIGURATION
# ==============================

# Define the size of the game window
# WIDTH controls horizontal space
# HEIGHT controls vertical space
WIDTH, HEIGHT = 700, 500



# List of possible turtle colors
# Each racer will receive a different color
# The number of racers determines how many colors are selected
COLORS = [
    "blue",
    "red",
    "yellow",
    "green",
    "orange",
    "cyan",
    "white",
    "purple",
    "silver",
    "gold"
]





# ==============================
# PLAYER INPUT
# ==============================

# Function responsible for asking the player
# how many turtles should participate in the race
#
# Rules:
# - Minimum racers: 2
# - Maximum racers: 10
def get_number_of_turtles():


    # Keep asking until valid input is provided
    while True:


        # Get the number of racers from the player
        turtles = input(
            "Enter number of racers (2-10): "
        )



        # Check whether the input contains only numbers
        if turtles.isdigit():

            # Convert input from string to integer
            turtles = int(turtles)



        # Handle non-numeric input
        else:

            print("Enter numeric number only")



        # Check if the number is within the allowed range
        if 2 <= turtles <= 10:

            # Return the valid racer count
            return turtles



        else:

            print("You're out of range (2-10)")





# ==============================
# GAME WINDOW SETUP
# ==============================

# Function responsible for creating and configuring
# the turtle graphics window
def init_turtle():


    # Create the turtle screen
    screen = turtle.Screen()



    # Set the size of the window
    screen.setup(
        WIDTH,
        HEIGHT
    )



    # Give the game a title
    screen.title(
        "Ghislain's turtle game"
    )



    # Set background color
    screen.bgcolor(
        "black"
    )





# ==============================
# RACE ENGINE
# ==============================

# Function responsible for running the actual race
#
# It:
# 1. Creates turtles
# 2. Moves them randomly
# 3. Checks the winner
#
# Returns:
# The color of the winning turtle
def race(colorr):


    # Create all turtle racers and place them
    # at their starting positions
    turtles = create_turtles(colorr)



    # Continue the race until somebody wins
    while True:


        # Give every turtle a chance to move
        # Each turtle moves one after another
        for racer in turtles:


            # Generate random movement distance
            #
            # Small random values create unpredictable racing
            distance = random.randrange(
                1,
                20
            )



            # Move the turtle forward
            racer.forward(distance)



            # Get current turtle position
            #
            # x = horizontal position
            # y = vertical position
            x, y = racer.pos()



            # Check if turtle reached the finish line
            #
            # The finish line is near the top of the screen
            if y >= HEIGHT // 2 - 30:


                # Find which turtle won
                #
                # Return its matching color
                return colorr[
                    turtles.index(racer)
                ]





# ==============================
# TURTLE CREATION
# ==============================

# Function responsible for creating all racer turtles
# and placing them at the starting line
def create_turtles(colors):


    # Empty list to store all created turtle objects
    turtles = []



    # Calculate horizontal spacing between racers
    #
    # Example:
    # If there are 5 turtles,
    # divide screen width into equal positions
    spacingX = WIDTH // (
        len(colors) + 1
    )



    # Create one turtle for every selected color
    #
    # enumerate gives:
    #
    # index → position number
    # color → turtle color
    for i, color in enumerate(colors):


        # Create a new turtle object
        racer = turtle.Turtle()



        # Assign the turtle's color
        racer.color(color)



        # Change appearance from arrow to turtle
        racer.shape(
            "turtle"
        )



        # Rotate turtle upward
        # because the race happens vertically
        racer.left(90)



        # Disable drawing lines while moving
        racer.penup()



        # Position turtle at starting line
        #
        # Each turtle gets a different horizontal position
        racer.setpos(
            -WIDTH // 2 + (i + 1) * spacingX,
            -HEIGHT // 2 + 20
        )



        # Save turtle object for later movement
        turtles.append(racer)



    # Return all created racers
    return turtles





# ==============================
# GAME START
# ==============================


# Ask player how many racers they want
answer = get_number_of_turtles()



# Create and configure the game window
init_turtle()



# Randomize available colors
# This prevents the same turtle order every game
random.shuffle(
    COLORS
)



# Select only the required number of colors
#
# Example:
# Player chooses 3 racers:
# ["blue", "red", "yellow"]
colorr = COLORS[:answer]



# Start the race
# Store the returned winner
winner = race(colorr)



# Display the winner
print(
    f"The winner is {winner}"
)



# Wait two seconds before closing
time.sleep(2)