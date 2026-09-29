import support
import viewing

# Function for adding a word and its translation to the list
def adds():
    support.clear()

    viewing.looksL()
    listName = input("Enter the name of the required list")
    if listName in support.Lists:
    
        key = input("Enter a word in English: ")
        print(f"Word: {key}")
        value = input("Enter the translation of the word in German AND the article(example: die Tasche): ")
        support.Lists[listName][key] = value
        print("Word added")
        support.press()
    else:

        print("This list doesn't exist.")
        support.press()
