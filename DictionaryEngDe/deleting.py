import support
import viewing

def delete():
    viewing.looks()
    deleteW = input("Enter the English word to delete:")
    del support.Words[deleteW]
    print("Word deleted")
    support.press()