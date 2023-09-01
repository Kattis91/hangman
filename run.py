import random

import time

import sys

from hangman import HANGMAN_LEVELS

from words import words


print("====================================\n"
      " Welcome to the HANGMAN game!\n\n"
      " The game is about guessing\n"
      " letters in a word. At the beginning\n"
      " of the game, letters are hidden.\n"
      " Once guessed, they are revealed\n"
      " in their actual posititons.\n\n"
      " 1. You will have 9 attempts\n"
      " 2. You can play several times\n"
      "====================================\n")


def validate_username():
    """
    Validates the username to ensure that a player enters a name
    with at least one letter.
    Checks that nothing else than letters are entered.
    """
    while True:
        try:
            username = input("Please enter your name: ")
            if username.isalpha():
                print(f"\nHi {username} \U0001F44B. Are you ready to play?\n")
                break
            raise TypeError
        except TypeError:
            print("NOTE: Only letters are accepted!\n")
            print("\nPlease enter a name containing at least one letter.")
            continue


validate_username()


def get_player_choice():
    """
    Runs a while loop to collect data from the playes, which must be yes or no.
    The loop will repeatedly request data until we get yes or no.
    """
    player_choice = input("yes / no: ")

    while True:
        if player_choice.lower().strip() == "no":
            print("\nYou are welcome back another time. Have a nice day!")
            sys.exit()
        if player_choice.lower().strip() == "yes":
            print("\nLet's go then...\U0001F60E")
            break
        print(f"\nYou entered {player_choice}, please enter 'yes' or 'no'\n")
        player_choice = input("yes / no: ")


get_player_choice()


def get_word():
    """
    Gets and returns a random word from the words list
    """
    return random.choice(words).upper()


time.sleep(1)
print("\nThe game begins in...\n")
time.sleep(1)
print("3\n")
time.sleep(1)
print("2\n")
time.sleep(1)
print("1\n")


print(HANGMAN_LEVELS[0])


def start_game(chosen_word):
    """
    Hides the word and shows it with the help of underscores.
    One underscore for each letter in the word
    """
    hidden_word = ['_' for i in range(len(chosen_word))]
    print(' '.join(hidden_word))


def check(chosen_word, guess):
    """
    Checks whether the letter guessed by the player is in the word.
    Returns true if the letter is in the word, returns false if it is not
    """
    if guess in chosen_word:
        return True
    return False


already_guessed = []
already_shown = []


def validate_data(chosen_word):
    """
    Takes in a players's guess. Validates data from the input and ensures
    that the player enters one letter at each guess.
    Checks if the letter was already guessed, and if it is,
    asks the player for a new letter. Puts all new guesses in a list.
    Tells the player whether the guessed letter is in the word or not.
    Prints out the next hangman_level and counts down the number of attempts
    for each guess that is not correct.
    Tells the player the word when all the attempts are used.
    """
    guess = None
    max_attempts = 9
    game_over = False

    hidden_word = ["_" for i in range(len(chosen_word))]

    while not game_over:
        guess = input("\n\nEnter a letter: ").upper()

        if len(guess) == 1 and guess.isalpha():
            result = check(chosen_word, guess)
            if guess in already_guessed:
                print(f"\nYou've already guessed letter {guess}. Try again!\n")
            elif result:
                print(f"\nYes, letter {guess} is in the word!\n")
                already_guessed.append(guess)
                already_shown.append(guess)
            else:
                print(f"\nSorry... letter {guess} is not in the word.")
                already_guessed.append(guess)
                max_attempts -= 1
                print(f"\nYou have {max_attempts} attempts left")
                print(HANGMAN_LEVELS[(len(HANGMAN_LEVELS) - 1) - max_attempts])
                if max_attempts == 0:
                    print(f"The word is {chosen_word}\n")
                    game_over = True
                    already_shown.clear()
                    already_guessed.clear()
        else:
            print("\nYou need to enter A LETTER.\n")

        show_the_letter(chosen_word)

        # loops over the chosen_word, and if the letter guessed is
        # in chosen_word, replaces index with the guessed letter.
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                hidden_word[index] = letter
        # checks if all the letters are guessed, and if it is,
        # finishes the game and prints a message to the user.
        if "_" not in hidden_word:
            game_over = True
            print("\n\nCongratulations! You won the game! GOOD JOB!\U0001F973")
            already_shown.clear()
            already_guessed.clear()

    return show_game_over() if game_over else guess


def show_the_letter(chosen_word):
    """
    Replaces underscores with letters when a user guesses correctly
    """
    for letter in chosen_word:
        if letter in already_shown:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def show_game_over():
    """
    Asks if a player wants to play again.
    Takes over only when game_over is True
    """
    play_again = input("\n\nWould you like to play again?\n\n")
    while True:
        if play_again.lower().strip() == "yes":
            main()
            break
        if play_again.lower().strip() == "no":
            print("\nWelcome back another time!")
            sys.exit()
        print("\n\nWas it 'yes' or 'no'?\n\n")
        play_again = input("Would you like to play again?\n\n")
        continue


def main():
    """
    Runs all program functions
    """

    chosen_word = get_word()
    start_game(chosen_word)
    validate_data(chosen_word)


main()
