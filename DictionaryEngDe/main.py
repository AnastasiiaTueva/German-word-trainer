import os
import support
import deleting
import adding
import viewing
import lists

# Main program loop
while True:

    # Function for clearing the console
    support.clear()

    # Display the menu
    support.Menu()

    # Main command input
    command = input("Enter a command: ").lower()

    match command:

        case "play":
            pass

        case "add word":

            adding.adds()

        case "add list":

            lists.addsL()

        case "delete":
            deleting.delete()

        case "look":
            viewing.looks()
            viewing.looksL()

        case "exit":

            break
