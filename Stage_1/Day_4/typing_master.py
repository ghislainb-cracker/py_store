# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================

# Import curses because it allows us to create
# interactive terminal interfaces:
# - colors
# - cursor movement
# - real-time keyboard input
import curses


# Import wrapper because it safely initializes
# and closes the curses environment
from curses import wrapper


# Import time because we need to measure
# how long the user takes to finish typing
import time


# Import random because the program selects
# a random typing paragraph from a file
import random





# ==============================
# START SCREEN
# ==============================

# Function responsible for displaying
# the welcome page before the typing test begins
#
# Parameter:
# stdscr → the terminal screen object provided by curses
def start_screen(stdscr):


    # Remove anything currently displayed
    stdscr.clear()



    # Display the title message
    # color_pair(1) applies the green color style
    stdscr.addstr(
        0,
        0,
        "Welcome to the speed typing test!",
        curses.color_pair(1)
    )



    # Display instructions
    stdscr.addstr(
        1,
        0,
        "Press any key to continue"
    )



    # Update the terminal screen
    stdscr.refresh()



    # Wait until the user presses a key
    # before continuing to the typing test
    stdscr.getkey()





# ==============================
# DISPLAY TYPING INTERFACE
# ==============================

# Function responsible for drawing:
# - target sentence
# - user's current typing
# - mistakes
# - WPM score
#
# It compares every typed character
# against the correct character
def display_text(
    stdscr,
    target,
    current,
    wpm=0
):


    # Display the original sentence
    # the player needs to type
    stdscr.addstr(
        target
    )



    # Display current typing speed
    stdscr.addstr(
        1,
        0,
        f"WPM: {wpm}"
    )



    # Check every character typed by the user
    for i, char in enumerate(current):


        # Get the correct character
        # from the target sentence
        correct_char = target[i]



        # Assume character is correct
        # so use green color
        color = curses.color_pair(1)



        # If typed character does not match
        # highlight it as a mistake
        if char != correct_char:

            color = curses.color_pair(2)



        # Replace the displayed character
        # with the user's typed version
        # using the correct color
        stdscr.addstr(
            0,
            i,
            char,
            color
        )





# ==============================
# TEXT LOADING SYSTEM
# ==============================

# Function responsible for getting
# a random typing paragraph
# from an external file
def load_text():


    # Open the file containing
    # possible typing sentences
    with open(
        "test.txt",
        "r"
    ) as file:


        # Read every line from the file
        lines = file.readlines()



        # Select one random sentence
        # and remove extra spaces/newlines
        return random.choice(lines).strip()





# ==============================
# MAIN TYPING ENGINE
# ==============================

# Function controlling the actual typing test
#
# Responsibilities:
# 1. Load text
# 2. Receive keyboard input
# 3. Track time
# 4. Calculate WPM
# 5. Detect completion
def wpm_test(stdscr):


    # Get the sentence the player must type
    target_text = load_text()



    # Store every character typed by the user
    #
    # Example:
    # ['H', 'e', 'l', 'l', 'o']
    current_text = []



    # Starting typing speed
    wpm = 0



    # Save the exact moment typing begins
    start_time = time.time()



    # Enable non-blocking keyboard input
    #
    # The program will not freeze waiting
    # for a key press
    stdscr.nodelay(True)



    # Main typing loop
    while True:


        # Calculate how many seconds passed
        #
        # max(...,1) prevents division by zero
        time_elapsed = max(
            time.time() - start_time,
            1
        )



        # Calculate words per minute
        #
        # Standard formula:
        #
        # characters / 5 = words
        #
        # words / minutes = WPM
        wpm = max(
            0,
            (len(current_text) / 5)
            /
            (time_elapsed / 60)
        )



        # Clear old display
        stdscr.clear()



        # Draw updated typing interface
        display_text(
            stdscr,
            target_text,
            current_text,
            wpm
        )



        # Refresh screen with new changes
        stdscr.refresh()



        # Check whether the player completed
        # the entire sentence
        if "".join(current_text) == target_text:


            # Return keyboard input to normal mode
            stdscr.nodelay(False)



            # End typing test
            break



        # Try receiving keyboard input
        try:

            key = stdscr.getkey()



        # When no key is pressed,
        # continue the loop
        except:

            continue





        # ESC key exits the typing test
        if ord(key) == 27:
            break



        # Handle deleting characters
        #
        # Allows user to correct mistakes
        if key in (
            "KEY_BACKSPACE",
            "\b",
            "\X7f"
        ):


            # Only delete if
            # there is something typed
            if len(current_text) > 0:

                current_text.pop()



        # Add normal characters
        #
        # Prevent typing beyond
        # the sentence length
        elif len(current_text) < len(target_text):

            current_text.append(key)





# ==============================
# APPLICATION CONTROLLER
# ==============================

# Main program function
# Controls screens and game rounds
def main(stdscr):


    # Create color theme:
    #
    # Pair 1:
    # correct characters → green
    curses.init_pair(
        1,
        curses.COLOR_GREEN,
        curses.COLOR_BLACK
    )



    # Pair 2:
    # incorrect characters → red
    curses.init_pair(
        2,
        curses.COLOR_RED,
        curses.COLOR_BLACK
    )



    # Pair 3:
    # additional white style
    curses.init_pair(
        3,
        curses.COLOR_WHITE,
        curses.COLOR_BLACK
    )



    # Show welcome screen
    start_screen(stdscr)



    # Keep allowing multiple rounds
    while True:


        # Start typing test
        wpm_test(stdscr)



        # Clear screen after completion
        stdscr.clear()



        # Show completion message
        stdscr.addstr(
            2,
            0,
            "You completed the text! Press any key to continue..."
        )



        # Update screen
        stdscr.refresh()



        # Wait for user response
        key = stdscr.getkey()



        # Exit if ESC key pressed
        if stdscr.getkey() == 27:

            break





# ==============================
# PROGRAM ENTRY POINT
# ==============================

# Start curses application safely
wrapper(main)