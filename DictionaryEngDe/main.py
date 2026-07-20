import os
import support
import deleting
import adding
import viewing
import lists


while True:
    support.clear()
    support.Menu()
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