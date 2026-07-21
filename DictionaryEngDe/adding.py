import support
import viewing

def adds():
    support.clear()

    viewing.looksL()
    listName = input("Enter the name of the required list: ")
    if listName in support.Lists:
        support.clear()
        key = input("Enter a word in English: ")
        print(f"Word: {key}")
        value = input("Enter the translation of the word in German AND the article(example: die Tasche): ")
        support.Lists[listName][key] = value
        support.clear()
        print("Word added")
        support.press()
    else:

        print("This list doesn't exist.")
        support.press()
