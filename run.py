import random

from hangman import HANGMAN_LEVELS

from words import words


print("============================================================\n"
       "Welcome to the Hangman game! The game involves guessing\n" 
       "letters in a word. Letters are initially completely hidden\n" 
       "but are shown as clues when you successfully guess them.\n" 
                       "\n"
       "        1.You will play with random words\n"
       "        2.You will have 9 attempts\n"
       "        3.You can play several times\n"
      "============================================================\n")

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
            quit()
            break
        elif user_choice.lower() == "yes":
            print("\nLet's go then...")
            break
        else:
            print(f"\nYou entered {user_choice}, please enter 'yes' or 'no'\n")
            user_choice = input("yes / no: ")
            continue   


get_user_info()


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
    print(chosen_word)


def check(chosen_word, guess):
    """
    Checks whether the letter guessed by the user is in the word.
    Returns true if the letter is in the word, returns false if it is not
    """
    if guess in chosen_word:
        return True
    return False


already_guessed = []
already_shown = []


def validate_data(chosen_word):
    """
    Takes in user's guess. Validates data from the input and ensures
    that the user enters one letter at each guess.
    Checks if the letter was already guessed, and if it is,
    asks user for a new letter. Puts all new guesses in a list.
    Tells the user whether the guessed letter is in the word or not.
    Prints out the next hangman_level and counts down the number of attempts
    for each guess that is not correct.
    Tells user the word when all the attempts are used. 
    """
    guess = None
    max_attempts = 9
    game_over = False
       
    while not game_over:
        guess = input("\n\nEnter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            result = check(chosen_word, guess)
            if guess in already_guessed:
                print(f"\nYou have alredy guessed {guess}. Try again!\n")
            elif result:
                print(f"\nYes, {guess} is in the word!")
                already_guessed.append(guess)
                already_shown.append(guess)
            else:
                print(f"\nThe letter {guess} is not in the word.")
                already_guessed.append(guess)
                max_attempts -= 1
                print(f"\nYou have {max_attempts} attempts left")
                print(HANGMAN_LEVELS[(len(HANGMAN_LEVELS) - 1) - max_attempts])
                if max_attempts == 0:
                    print(f"The word is {chosen_word}\n")
                    game_over = True    
        else:
            print("You need to enter A LETTER. ")
        
        show_the_letter(chosen_word)
             
    return show_game_over() if game_over else guess


def show_the_letter(chosen_word):
    """
    Replaces underscores with letters when user guesses correct
    """
    for letter in chosen_word:
        if letter in already_shown:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def show_game_over():
    """
    Asks if user wants to play again.
    Takes over only when game_over is True
    """
    play_again = input("Would you like to play again?")
    while True:
        if play_again == "yes":
            main()
            break
        elif play_again == "no":
            print("Welcome back another time!")
            break
            exit()   
        else:
            print("Was it 'yes' or 'no'?")
            play_again = input("Would you like to play again?")
            continue


def main():
    """
    Runs all program functions
    """
    chosen_word = get_word()
    start_game(chosen_word)
    validate_data(chosen_word)
 
main()

