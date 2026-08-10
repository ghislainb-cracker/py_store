# Open the story file and read its content
with open("story.txt", "r") as file:
    story = file.read()

# Create a set to store the special words that need to be replaced
words = set()
start_of_word = -1

# Define the characters that mark the beginning and end of a placeholder word
start_target = "<"
ending_target = ">"

# Scan the story character by character and find every placeholder word
for i, char in enumerate(story):
    # If we find the opening marker, remember where the word started
    if char == start_target:
        start_of_word = i

    # If we find the closing marker, collect the full placeholder word
    if char == ending_target and start_of_word != 1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Create an empty dictionary to store the user's answers
answers = {}

# Ask the user to replace each placeholder word
for word in words:
    answer = input(f"Replace the word given, {word}: ")
    answers[word] = answer

# Replace every placeholder in the story with the user's answer
for word in words:
    story = story.replace(word, answers[word])

# Print the completed story
print(story)
