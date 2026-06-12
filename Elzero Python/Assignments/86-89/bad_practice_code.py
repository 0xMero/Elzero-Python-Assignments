""" This Module or file is an asssignment of elzero,
It ask me to fix the bad practices made in this code"""
# Assignment 5
MYFRIENDS = ["Ahmed", "Osama", "Sayed"]
def say_hello(some_peoples) -> list:
    """ This Function is designed to say hello to the person"""
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(MYFRIENDS)
