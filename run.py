import random

def get_user_info():
    """
    Gives a user the opportunity to enter a username and to choose whether
    to start the game or to quit
    """
    username = input("Please enter your name: ")
    print(f"\nHello {username}, are you ready to play?\n")
    user_choice = input("yes / no: ")

get_user_info()