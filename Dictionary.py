import os
import random

Words = {}
points = 0

def press():
    input("Press any key to continue....")

def clear():
    os.system('cls')

def adds():
    clear()
    key = input("Enter a word in English: ")
    print(f"Word: {key}")
    value = input("Enter the translation of the word in German: ")
    Words[key] = value
    print("Word added")
    press()
    

def looks():
    clear()
    print("English word - German word:\n"
    "------------------------------")
    for key, value in Words.items():

        print(f"{key} - {value}")
    press()

    
    
    
def Menu():
    print("English-German Dictionary")
    print("--------------------------------------------")
    print("Play - play the mini-game. \n"
        "Add - add a word and its translation to the dictionary \n"
        "Delete - remove a word and its translation from the dictionary \n" \
        "Look - view the dictionary \n" \
        "Exit - exit the program")
    print("--------------------------------------------")

def deleting():
    deleteW = input("Enter the English word to delete:")
    del Words[deleteW]
    print("Word deleted")
    press()



while True:
    clear()
    Menu()
    command = input("Enter a command: ").lower()
    match command:
        case "play":
            pass


        case "add":

            adds()

        case "delete":
            looks()
            deleting()

        case "look":

            looks()

        case "exit":

            break
