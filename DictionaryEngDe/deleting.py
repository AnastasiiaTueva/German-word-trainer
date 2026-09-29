import support
import viewing

# Function for removing a word and its translation from the list
def delete():
    viewing.looks()
    deleteW = input("Enter the English word to delete:")
    del support.Words[deleteW]
    print("Word deleted")
    support.press()
