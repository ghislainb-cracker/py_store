# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================

# Import playsound so the program can play an audio file
# when the countdown reaches zero
from playsound import playsound


# Import time because the program needs to pause execution
# for one second between countdown updates
import time





# ==============================
# TERMINAL DISPLAY CONTROL
# ==============================

# Special terminal escape character sequence
# Used to clear the terminal screen completely
CLEAR = "\033[2J"


# Special terminal escape sequence
# Moves the cursor back to the top-left position
#
# This allows us to update the countdown in the same place
# instead of printing a new line every second
CLEAR_AND_RETURN = "\033[H"





# ==============================
# ALARM COUNTDOWN FUNCTION
# ==============================

# Function responsible for:
# 1. Counting down the remaining time
# 2. Displaying the countdown
# 3. Playing the alarm sound at the end
#
# Parameter:
# seconds → total countdown duration in seconds
def alarm(seconds):


    # Track how much time has already passed
    # Starts at zero because the countdown has not started yet
    time_elapsed = 0



    # Clear the terminal before displaying countdown
    print(CLEAR)



    # Continue running until all requested seconds have passed
    while time_elapsed < seconds:


        # Pause the program for exactly one second
        # This creates the countdown effect
        time.sleep(1)



        # Increase elapsed time after one second passes
        time_elapsed += 1



        # Calculate how much time remains
        #
        # Example:
        # total = 120 seconds
        # elapsed = 10 seconds
        #
        # remaining = 110 seconds
        time_left = seconds - time_elapsed



        # Convert remaining seconds into minutes
        #
        # Example:
        # 125 seconds
        # 125 // 60 = 2 minutes
        minutes_left = time_left // 60



        # Get remaining seconds after removing full minutes
        #
        # Example:
        # 125 seconds
        # 125 % 60 = 5 seconds
        seconds_left = time_left % 60



        # Display the remaining countdown time
        #
        # {minutes_left:02d}
        # means:
        # always show two digits
        #
        # Example:
        # 3 becomes 03
        #
        # Output:
        # Alarm will sound in 02:05
        print(
            f"{CLEAR_AND_RETURN}"
            f"Alarm will sound in "
            f"{minutes_left:02d}:{seconds_left:02d}"
        )



    # When countdown finishes:
    # Play the alarm audio file
    playsound(
        "sound.wav"
    )





# ==============================
# USER INPUT
# ==============================


# Ask the user how many minutes they want the timer to run
minutes = int(
    input(
        "How many minutes to wait: "
    )
)



# Ask the user how many additional seconds they want
seconds = int(
    input(
        "How many seconds to wait: "
    )
)



# Convert the user's input into one unit (seconds)
#
# Formula:
#
# total seconds =
# (minutes × 60) + remaining seconds
#
# Example:
# 2 minutes and 30 seconds:
#
# (2 × 60) + 30 = 150 seconds
total_seconds = (
    minutes * 60
    + seconds
)



# Start the countdown timer
alarm(
    total_seconds
)