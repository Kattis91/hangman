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
            exit()
        elif user_choice.lower() == "yes":
            print("\nLet's go then...")
            break 
        else:
            print(f"\nYou entered {user_choice}, please enter 'yes' or 'no'\n")
            user_choice = input("yes / no: ")
            continue   


get_user_info()


HANGMAN_LEVELS = [ 
"""
  _ _ _ _ _ _ _ _
  |             |
  |             
  |            
  |            
  |             
  |                       
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             
  |            
  |             
  |                    
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |            
  |             
  |                       
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |             |
  |             
  |                      
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |            \|
  |             
  |                        
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |            \|/
  |             
  |                      
  |
  |     
  |
=====
""",
""" 
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |            \|/
  |             |
  |                      
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |            \|/
  |             |
  |            /             
  |
  |     
  |
=====
""",
"""
  _ _ _ _ _ _ _ _
  |             |
  |             |
  |             O
  |            \|/
  |             |
  |            / \            
  |
  |     G A M E  O V E R!
  |
=====
"""
]

words = ["orange", "weakness", "improvement", "tradition", "television",
       "friendship", "argument", "consequence", "replacement", "teacher",
       "software", "energy", "alcohol", "employer", "reaction", "airport",
       "strategy", "teaching", "leadership", "system", "perception",
       "description", "efficiency", "literature", "assignment", "speech",
       "painting", "initiative", "committee", "proposal"]


def get_word():
    """
    Gets and returns a random word from the words list
    """
    return random.choice(words)


print("\nThe game now begins...3...2...1")
print(HANGMAN_LEVELS[0])


def start_game(chosen_word):
    """
    Hides the word and shows it with the help of dashes.
    One dash for each letter in the word
    """
    hidden_word = ['_' for i in range(len(chosen_word))]
    print(' '.join(hidden_word))


def validate_data(chosen_word):
    """
    Takes in users guess...
    """
    guess = input("\nEnter a letter: ").lower()


chosen_word = get_word()
start_game(chosen_word)
validate_data(chosen_word)

