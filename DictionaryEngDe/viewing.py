import support
import lists

def looks():
    support.clear()
    print("English word - German word:\n"
    "------------------------------")
    for key, value in support.Words.items():

        print(f"{key} - {value}")
    support.press()

def looksL():
    support.clear()
    print("Your lists:\n"
    "------------------------------")
    for name in support.Lists:
        print(name)

    support.press()