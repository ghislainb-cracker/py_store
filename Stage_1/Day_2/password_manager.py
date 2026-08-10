# Import Fernet encryption system from the cryptography library
# Fernet provides symmetric encryption:
# - The same secret key is used to encrypt and decrypt information
# - Useful for protecting sensitive data like passwords
from cryptography.fernet import Fernet



# Function responsible for creating and saving the encryption key
# This key acts like the "lock" used to protect our passwords
def write_key():

    # Generate a random secure encryption key
    # Every time this runs, a completely new key is created
    key = Fernet.generate_key()


    # Open a file called "key.key" in binary write mode
    # "wb" means write bytes because encryption keys are stored as bytes
    with open("key.key", "wb") as key_file:

        # Save the generated secret key inside the file
        key_file.write(key)



# Create the encryption key when the program starts
# Normally this should only happen once,
# because generating a new key would make old encrypted passwords impossible to read
write_key()



# Function responsible for loading the saved encryption key
# The program needs this key later to decrypt stored passwords
def load_key():

    # Open the key file in binary read mode
    file = open("key.key", "rb")


    # Read the stored encryption key
    key = file.read()


    # Close the file to free system resources
    file.close()


    # Return the key so the program can use it
    return key



# Ask the user for a master password
# This acts as an additional layer of protection
# Only someone who knows this password should access saved passwords
master_pwd = input("Enter your master password: ")



# Combine the saved encryption key with the user's master password
# The idea is to create a stronger secret key
# The password is converted from text into bytes because encryption works with bytes
keyy = load_key() + master_pwd.encode()



# Create a Fernet encryption object
# This object contains the encryption/decryption logic
# We will use it whenever we save or retrieve passwords
fer = Fernet(keyy)




# Function responsible for displaying saved passwords
def view():


    # Open the password storage file in read mode
    # This file contains:
    # username|encrypted_password
    with open("user_password.txt", "r") as f:


        # Read every saved password entry one by one
        for lines in f.readlines():


            # Remove unnecessary spaces and newline characters
            data = lines.rstrip()


            # Split each line into two pieces:
            # username and encrypted password
            #
            # Example:
            # john|gAAAAABl...
            #
            # becomes:
            # usr = john
            # passwd = encrypted password
            usr, passwd = data.split("|")


            # Decrypt the encrypted password
            # Convert encrypted text back into bytes
            # Then convert bytes back into readable text
            decrypted_password = fer.decrypt(
                passwd.encode()
            ).decode()


            # Display the username and original password
            print(
                f"username: {usr}, password: {decrypted_password}"
            )





# Function responsible for adding a new password entry
def add():


    # Ask the user for the account username
    user = input("Enter user name: ")


    # Ask the user for the password they want to store
    pwd = input("Enter password: ")



    # Open password storage file in append mode
    # "a" means add new information without deleting previous passwords
    with open("user_password.txt", "a") as f:


        # Encrypt the password before saving
        # Never store passwords as plain text
        encrypted_password = fer.encrypt(
            pwd.encode()
        ).decode()



        # Store data in this format:
        #
        # username|encrypted_password
        #
        # Example:
        # gmail_user|gAAAAABl8....
        f.write(
            user + "|" + encrypted_password + "\n"
        )





# Main program loop
# Keeps the password manager running until the user chooses to exit
while True:


    # Ask the user what action they want to perform
    user_operation = input(
        "Do you want to view or add a new password - (view, add, or q to quit) "
    ).lower()



    # Exit condition:
    # If user types q, stop the infinite loop
    if user_operation == "q":
        break



    # If user chooses view:
    # Show all stored passwords after decrypting them
    if user_operation == "view":
        view()



    # If user chooses add:
    # Encrypt and save a new password
    elif user_operation == "add":
        add()



    # Handle invalid commands
    else:
        print("Please enter a valid option")