import support

#Function for creating a word list
def addsL():
    support.clear()
    name = input("Enter a list name: ")
    support.Lists[name] = {}
    print("The list has been created.")
    support.press()
