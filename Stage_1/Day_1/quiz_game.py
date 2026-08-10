print("Hello Welcome to the Quiz Game")

# Ask the player if they want to start the quiz
continue_game = input("Do you want to play game?(Y/N): ").lower()

# Stop the program if the player says no
if continue_game == "n":
    quit()

# Start with zero points
score = 0

print("Let me trick your mind now :)")

# Question 1: CPU
answer = input("What CPU stand for: ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")

# Question 2: GPU
answer = input("What GPU stand for: ").lower()
if answer == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")

# Question 3: RAM
answer = input("What RAM stand for: ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("incorrect")

# Show the final score and percentage
print(f"you scored {score} questions")
print("you got " + str(round((score * 100) / 3)) + "%")
