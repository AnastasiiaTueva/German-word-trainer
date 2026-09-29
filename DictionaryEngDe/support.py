import os

# List creation
Words = {}
Lists = {}
points = 0

# Function that pauses the program after displaying the result until a key is pressed
def press():
    input("Press any key to continue....")

# Function for clearing the console
def clear():
    os.system('cls')

# Function for formatting the program menu
def Menu():
    print("English-German Dictionary")
    print("--------------------------------------------")
    print("Play - play the mini-game. \n"
        "Add Word - add a word and its translation to the dictionary \n"
        "Add List - add a new list \n"
        "Delete - remove a word and its translation from the dictionary \n" \
        "Look - view the dictionary and lists \n" \
        "Exit - exit the program")
    print("--------------------------------------------")
