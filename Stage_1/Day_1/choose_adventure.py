# ask a user the name
name = input("Type your name: ")
# wleocome name to the game
print("Welcome", name, "to this adventure!")

# ask him/her choose where to firstly go between left or right s he/she found him/her on the end of the dirty road 
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
# check if answer is left
if answer == "left":
    # let him choose between swimming across or walk around the river
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    # check if the answer is swim, tell him/her that he/she is eaten by an alligator
    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    # if answer is walk, tell him/her that he/she walked for many miles and ran out of water and losy the game
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    # else it is an invalid input
    else:
        print('Not a valid option. You lose.')

# also check if answer is right
elif answer == "right":
    # ask the user the cross or head back to the bridge
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    # check if an answer is back
    if answer == "back":
        # print that yougo back and lose
        print("You go back and lose.")
    # check if answer is cross
    elif answer == "cross":
        # ask him/her is to talk with the stranger that he/she met after crossing the bridge
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        # check if answer is yes
        if answer == "yes":
            # print the stranger gives gold and you won!
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            # tell the user that he/she loses the game 
            print("You ignore the stranger and they are offended and you lose.")
        else:
            # else invalid input and lose
            print('Not a valid option. You lose.')
    else:
        # else invalid input and lose
        print('Not a valid option. You lose.')

else:
    # else invalid input and lose
    print('Not a valid option. You lose.')
# thanks the user for trying  + name
print("Thank you for trying", name)