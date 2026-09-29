import support
import lists

# Functions for displaying word lists and lists in general
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
    print("------------------------------")
    support.press()
