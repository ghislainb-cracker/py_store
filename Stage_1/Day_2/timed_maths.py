# Import random because the game needs to generate unpredictable maths questions
# Import time because we need to measure how long the player takes to finish
import random
import time



# ==============================
# GAME CONFIGURATION
# ==============================

# List of mathematical operations that can appear in questions
# The program will randomly choose one operation for every problem
OPERATORS = ["+", "-", "*"]


# Define the largest possible number that can appear in a question
MAX_OPERAND = 13


# Define the smallest possible number that can appear in a question
MIN_OPERAND = 3


# Define how many questions the player must answer before finishing
TOTAL_PROBLEMS = 10





# ==============================
# QUESTION GENERATOR
# ==============================

# Function responsible for creating one random maths problem
#
# It generates:
# 1. Left number
# 2. Right number
# 3. Mathematical operator
#
# Then it calculates the correct answer
#
# Example output:
# ("5 * 4", 20)
def generate_problem():


    # Generate the first random number within the allowed range
    left_operand = random.randint(
        MIN_OPERAND,
        MAX_OPERAND
    )


    # Generate the second random number within the allowed range
    right_operand = random.randint(
        MIN_OPERAND,
        MAX_OPERAND
    )


    # Randomly select one mathematical operator
    # Example: +, -, or *
    operator = random.choice(OPERATORS)



    # Build the question as a string
    #
    # Example:
    # left_operand = 5
    # operator = "+"
    # right_operand = 3
    #
    # Result:
    # "5 + 3"
    exp = (
        str(left_operand)
        + " "
        + operator
        + " "
        + str(right_operand)
    )



    # Calculate the correct answer automatically
    # eval() evaluates the mathematical expression
    #
    # Example:
    # eval("5 + 3") → 8
    answer = eval(exp)



    # Return both:
    # - the question shown to the player
    # - the correct answer used for checking
    return exp, answer





# ==============================
# GAME START
# ==============================


# Variable used to count how many incorrect attempts the player makes
# It increases every time the player enters a wrong answer
wrong = 0



# Pause the program until the player is ready
# This prevents the timer from starting before the player begins
input("Press Enter to start the game: ")


# Print a visual separator for better user experience
print("------------------------------------")



# Save the exact moment the quiz starts
# This will later be compared with the ending time
start_time = time.time()





# ==============================
# QUIZ LOOP
# ==============================


# Repeat the question process TOTAL_PROBLEMS times
#
# Example:
# TOTAL_PROBLEMS = 10
# The loop creates 10 questions
for i in range(TOTAL_PROBLEMS):


    # Generate a new random question and its answer
    exp, answer = generate_problem()



    # Keep asking until the player answers correctly
    # The player cannot move to the next question with a wrong answer
    while True:


        # Display the question number and maths expression
        #
        # Example:
        # question #1: 5 + 3 =
        user_answer = input(
            f"question #{i+1}: {exp} = "
        )



        # Compare the user's answer with the correct answer
        #
        # Convert answer to string because input() always returns text
        if user_answer == str(answer):

            # Correct answer:
            # Exit the loop and continue to the next question
            break



        # Wrong answer:
        # Increase the mistake counter
        wrong += 1





# ==============================
# RESULTS
# ==============================


# Record the exact moment when the quiz ends
end_time = time.time()



# Calculate the total duration of the game
#
# Formula:
# ending time - starting time = time taken
#
# round(..., 2) keeps only 2 decimal places
total_time = round(
    end_time - start_time,
    2
)



# Display final results
print("-------------------------------------")

print(
    f"Congratulations! You finished the game in: {total_time} sec"
)