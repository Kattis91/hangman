import random

def get_user_info():
    """
    Gives a user the opportunity to enter a username. 
    Runs a while loop to collect data from the user, which must be yes or no. 
    The loop will repeatedly request data until we get yes or no.
    """
    username = input("Please enter your name: ")
    print(f"\nHello {username}, are you ready to play?\n")
    user_choice = input("yes / no: ")

    while True:
        if user_choice.lower() == "no":
            print("\nYou are welcome back another time. Have a nice day!")
            break
        elif user_choice.lower() == "yes":
            print("\nLet's go then...")
            break
        else:
            print(f"\nYou entered {user_choice}, please enter 'yes' or 'no'\n")
            user_choice = input("yes / no: ")
            continue   

get_user_info()