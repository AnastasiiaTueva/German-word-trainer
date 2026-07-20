import support

def adds():
    support.clear()
    key = input("Enter a word in English: ")
    print(f"Word: {key}")
    value = input("Enter the translation of the word in German AND the article(example: die Tasche): ")
    support.Words[key] = value
    print("Word added")
    support.press()