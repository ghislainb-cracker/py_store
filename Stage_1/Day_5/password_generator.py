# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================

# Import random because passwords need unpredictable characters
# Random selection prevents generating the same password repeatedly
import random


# Import string because it provides ready-made character groups:
# - letters
# - numbers
# - symbols
import string





# ==============================
# PASSWORD GENERATION FUNCTION
# ==============================

# Function responsible for creating a random password
#
# Parameters:
#
# min_length:
#     Minimum number of characters required
#
# numbers:
#     Whether the password must contain numbers
#
# special_characters:
#     Whether the password must contain symbols
#
# Returns:
#     A randomly generated password that follows all rules
def generate_password(
    min_length,
    numbers=True,
    special_characters=True
):


    # Create a collection of possible characters
    #
    # ascii_letters contains:
    # abc...xyzABC...XYZ
    letters = string.ascii_letters



    # digits contains:
    # 0123456789
    digits = string.digits



    # punctuation contains symbols:
    # !@#$%^&*...
    special_chars = string.punctuation





    # Start with letters because every password
    # should have alphabetic characters available
    characters = letters



    # Add numbers to the available character pool
    # only if the user requested them
    if numbers:

        characters += digits



    # Add symbols to the available character pool
    # only if the user requested them
    if special_characters:

        characters += special_chars





    # Variable that stores the generated password
    # Starts empty because no characters have been selected yet
    pwd = ""



    # Tracks whether the password has satisfied all requirements
    # Starts false because the password is incomplete
    meets_criteria = False



    # Tracks whether at least one number exists
    has_number = False



    # Tracks whether at least one special character exists
    has_special = False





    # ==============================
    # PASSWORD CREATION LOOP
    # ==============================

    # Continue generating characters until:
    #
    # 1. Password reaches minimum length
    # AND
    # 2. Required character types exist
    #
    # Example:
    # Minimum length = 8
    # Must contain number
    # Must contain symbol
    #
    # Result:
    # "abc12@xy"
    while (
        not meets_criteria
        or len(pwd) < min_length
    ):



        # Select one random character
        # from the available character pool
        new_char = random.choice(
            characters
        )



        # Add the selected character
        # to the password
        pwd += new_char





        # Check if the new character is a number
        #
        # Example:
        # "A7"
        # 7 satisfies the number requirement
        if new_char in digits:

            has_number = True





        # Check if the new character is a symbol
        #
        # Example:
        # "@"
        # satisfies the special character requirement
        if new_char in special_chars:

            has_special = True





        # Assume requirements are satisfied
        # then update based on user settings
        meets_criteria = True



        # If numbers are required,
        # password must contain at least one number
        if numbers:

            meets_criteria = has_number



        # If symbols are required,
        # password must contain at least one symbol
        if special_characters:

            meets_criteria = (
                meets_criteria
                and has_special
            )





    # Return the final valid password
    return pwd





# ==============================
# USER CONFIGURATION
# ==============================


# Ask user for desired password length
password_length = int(
    input(
        "Enter the length of the password: "
    )
)



# Ask whether numbers should be included
#
# The comparison:
# input == "y"
#
# converts the answer into True or False
include_numbers = (
    input(
        "Should the password include numbers (y/n): "
    )
    .lower()
    == "y"
)



# Ask whether special characters should be included
include_chars = (
    input(
        "Should the password include special characters (y/n): "
    )
    .lower()
    == "y"
)





# ==============================
# GENERATE PASSWORD
# ==============================


# Call the password generator with the user's settings
pwd = generate_password(
    password_length,
    include_numbers,
    include_chars
)



# Display the generated password
print(pwd)