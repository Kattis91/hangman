# Hangman

Hangman is a Python terminal game, which runs oin the Code Institute mock terminal on Heroku.

Users get a possibility to play a guessing game even if they do not have someone around to play with.

![image](readme-images/am-i-responsive.jpg)

## How to play

 The player will have a total of nine attempts to correctly guess the word. Guessing multiple letters at once is not possible.If the playes enters a character other than a letter, they will receive an error message.

 When the player guess a letter, the game shows if it is correct and if it is, reveals its position in the word.

 If a letter is not in the word, a new image of the hangman is displayed, along with the number of attempts remaining.

 It is possible to play the game multiple times.

 ## Flowchart

 Flowchart was created using [Lucidchart](https://www.lucidchart.com/pages/sv).

 ![image](readme-images/flowchart.jpeg)

 ## Features 

 ### Welcome message

 ![image](readme-images/welcoming-message.jpg)
  
  - Tells a player what type of game it is.
  
  - Gives information about the game, amount of attempts, and the possibility to play several times.

  - Requests player's name.

### Name Validation

#### Input validation and error-checking:

![image](readme-images/name-validation.jpg)
  
  - A player can only enter letters.

  - Nothing else but letters are accepted. 

  - A name should contain at least ONE letter.


### Ready to play?

#### Once validation is complete, the user is given the option to choose either to play or not.

I know it's very early in the game, but what if a user accidentally stumbled upon the game or immediately regretted it?

![image](readme-images/hello-name.jpg)

  
 - The player chooses to play:

    - ![image](readme-images/ready-to-play.jpg)

       The game begins. Some time delay is added for animation feeling.

  - The player chooses NOT to play:
   
    - ![image](readme-images/not-ready-to-play.jpg)

      The game welcomes the player to come back another time.
  
  - The player enters something else than 'yes' or 'no':
    
    - ![image](readme-images/neither-yes-or-no.jpg)
      
      An error message appear on the screen asking the player enter either 'yes' or 'no'.

 
### Enter a letter

![image](readme-images/enter-a-letter.jpg)

  - This section shows the first hangman image.

  - A player gets to see the hidden word.

  - A player gets an opportunity to enter a letter.

  - Input validation: 
  
    - The letter is NOT in the word:

      ![image](readme-images/not-in-the-word.jpg)

       - A player gets a message with the information about that.

       - Information about how many attempts are left is displayed.

       - The next hangman image is displayed.

       - A player can guess the next letter as long as the game is still in progress. 
    
    - The letter is ALREADY guessed:

      ![image](readme-images/already-guessed.jpg)

       - A player gets a message with the information about that.

       - An opportunity to enter another letter appears on the screen.

    - The letter IS IN THE WORD:

      ![image](readme-images/letter-is-in-the-word.jpg)

       - A player gets a message with the information about that.

       - The game reveals the guessed letter's position in the word.

       - A player can guess the next letter as long as the game is still in progress. 


### The game is finished

#### What occurs when all letters are guessed or no attempts remain?

  - Game over:
   
    ![image](readme-images/game-over.jpg)

      - "You have 0 attempts left" message is displayed on the screen.

      - The last hangman image with the GAME OVER print is printed out for the player.

      - The player receives the information about the word that was previously hidden by the underscores.

      - The game asks whether the player wants to play again or not.

  - A player wins:

    ![image](readme-images/game-winner.jpg)

      - Congratulations message is printed out for the player.

      - The game asks whether the player wants to play again or not.


### Would you like to play again?

  - YES:
   
    ![image](readme-images/play-again.jpg)

     - A new random word that is currently hidden behind the underscores, appears on the screen.

     - A player gets an opportunity to enter a letter.

  - NO:

    ![image](readme-images/no-to-play-again.jpg)

    A "Welcome back another time!" message appears on the screen.

  - Was it YES or NO?

    ![image](readme-images/was-it-yes-or-no.jpg)
  
    If a player enters something else than 'yes' or 'no', a question repeatedly appears on the screen.

## User Stories 

### As a user I want to be able to:

 - read concise instructions to comprehend the game rules.
 - start a game when I am ready.
 - receive information on what went wrong in case I make an incorrect input.
 - know whether I guessed correctly or incorrectly or if the letter has already been guessed.
 - see the correctly guessed letter revealed in its correct position within the word.
 - see a new hangman image appear, as I guess incorrectly.
 - get information about how many attempts are left, as I guess incorrectly.
 - see the word I was guessing in case I lose the game.
 - start a new game when the current game has ended, regardless of whether I lost or won.
 
## Solved Bugs after Deployment:

  - When a player started a new round after losing, the letters that were correctly guessed in previous rounds were automatically entered as correctly guessed letters even for the new word. I solved the problem by resetting the list of correctly guessed letters every time a player loses the game.

  - When a player plays another round after losing, a message was displayed stating that a letter had already been guessed, even if it hadn't been guessed in that particular round. I solved the problem by resetting the list of all the guessed letters every time a player loses the game.

  - The same hangman image was displayed twice. The image was displayed at the beginning of the game. The same image was even displayed when the player guessed incorrectly for the first time. I solved this problem by adding one more image to the hangman list to make it work with indexes.

## Testing

### Validator testing

No errors were found when passing through the official [PEP8 Linter](https://pep8ci.herokuapp.com/).

### Manual Testing

| Feature | Expect | Action | Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Enter a name | When trying to input empty words, whitespaces, digits, symbols or a combination of letters and other characters, a player should receive an error message stating "Please enter a name containing at least one letter. NOTE: Only letters are accepted!". The message should repeat itself until a valid name is entered | Enter something else than only letters | A "Please enter a name containing at least one letter. NOTE: Only letters are accepted!" message appears on the screen. The message displays as long as the entered name doesn't contain only letters.| Pass
| Are you ready to play? (YES) | When a player chooses to play and writes "yes" in the terminal, "The game begins in..." counting down appears on the screen along with the first hangman image, hidden word, and the possibility to enter a letter. | Enter "yes" in the terminal. | The game starts with a countdown, followed by a hangman image and "Enter a letter" section.| Pass
| Are you ready to play? (NO) | When a player chooses not to play and writes "no" in the terminal, a player should receive a message stating "You are welcome back another time. Have a nice day!" | Enter "no" in the terminal | "You are welcome back another time. Have a nice day!" message appears on the screen. | Pass
| Are you ready to play? (Neither YES or NO) | When a player enters something else than "yes" or "no", a player should receive an error message stating "You entered {player_choice}, please enter 'yes' or 'no'". The message should repeat itself until 'yes' or 'no' is entered. ***{player_choice}** - _the player's specific input_. | Enter something else than 'yes' or 'no'. | "You entered {player_choice}, please enter 'yes' or 'no'" message appears on the screen until 'yes' or 'no' is entered | Pass
| Enter a letter. The letter is present in the word | When a player correctly guesses a letter, the game should display a message saying "Yes, letter {guess}* is in the word!" and reveal the letter in its correct position. ***{guess}** - _the player's input/guess_. | Enter a letter that is present in the word. It is possible to do that by printing out the "unhidden" word | "Yes, letter {guess} is in the word!" message appears on the screen, and the letter is printed out in its correct position. | Pass
| Enter a letter. The letter is NOT present in the word. | When a player inputs a letter that is not present in the word, the game should show a message saying "Sorry... letter {guess} is not in the word." Moreover, the game should show details regarding the remaining attempts and display the upcoming hangman image. | Enter a letter that is NOT present in the word. It is possible to find such a letter by printing out the "unhidden" word. | "Sorry... letter {guess} is not in the word." message appears on the screen. Information about amount of attempts and the next hangman image are displayed.| Pass
| Enter a letter. The letter has ALREADY been guessed. | When a player enters a letter that has already been guessed, the game should display a message that says "You've already guessed that letter. Please try again!" The message should continue to be displayed until a new letter is entered. | Enter a letter that has already been guessed. | "You've already guessed that letter. Please try again!" message is displayed. It keeps on displaying until an unguessed letter is entered. | Pass
| Game over | If all attempts are used and the word remains unguessed, the game will show a message "You have 0 attempts left". Additionally, the game should display the final image of the hangman with the words "GAME OVER" and the word that a player was trying to guess. | Use all the attempts by entering incorrect letters. To identify the incorrect letters, print out the word without any hidden characters. | "You have 0 attempts left" message is displayed on the screen along with the final "GAME OVER" hangman image and the word that was previously hidden. | Pass
| Congratulations! | When the final letter is guessed, the game should display a message that says "Congratulations! You won the game! GOOD JOB!" | Win the game by entering all the correct letters.To identify all the correct letters, print out the word without any hidden characters. | "Congratulations! You won the game! GOOD JOB!" message appears on the screen. | Pass 
| Would you like to play again? (YES) | When the player answers "yes," the game should display a new word and provide the option to input a letter. | Type "yes" into the terminal. | A new word and option to enter a letter appear on the screen. | Pass
| Would you like to play again? (YES) | When the player answers "no", the game should display a message saying "Welcome back another time!" | Type "no" into the terminal. | "Welcome back another time!" message displays on the screen. | Pass
| Would you like to play again? (Neither YES or NO) | When a player enters something other than "yes" or "no", the game should prompt them with a question asking if it was "yes" or "no". The question should continue to be displayed until the player types either "yes" or "no". | Type something into the terminal (something else than "yes" or "no"). | "Was it 'yes' or 'no'?" question appears on the screen. It keeps on displaying until either "yes" or "no" is entered. | Pass
| Resetting the lists | Regardless of whether the player wins or loses, the list with the correctly guessed words and the list with all guessed words should be cleared. | Print out both lists and see what happens with them when the game is finished. | Both lists gets empty ([]). | Pass


    
## Credits

### Media

Full Emoji List was found on [Unicode](https://unicode.org/emoji/charts/full-emoji-list.html).

### Content

  - [Random Word Generator](https://randomwordgenerator.com/) was used to generate random words.

  - I got the inspiration for my hangman images by the images shown in the [How to build HANGMAN with Python in 10 MINUTES](https://www.youtube.com/watch?v=m4nEnsavl6w) YouTube video.

  - Thanks to the Tutor Support for helping me finding a solution for looping over the word and replacing index with the guessed letter (if the letter guessed is in the word).

  - Instructions for replacing underscores with letters and revealing their correct positions in the word upon correct guesses come from [GeeksForGeeks](https://www.geeksforgeeks.org/python-program-for-word-guessing-game/).


## Deployment


 1. Sign up for Heroku and accept terms of service.

 2. Click the **"Create a new app"** button.

 3. Name the app (a name must be unique) and choose a region.

 4. Create a _Config Var_ with the key **PORT** and the value **8000**.

 5. Click **"Add buildpack"** and the following buildpacks (in the order presenting):
     - Python
     - NodeJS

 6. Click on the **"Deploy"** section on the top of the page.

 7. Select **GitHub** as deployment method and click **"The connect to GitHub"** button.

 8. Search for the repository for this project, _hangman_. 

 9. Click **"Connect"** to link up Heroku app to the GitHub repository.

 10. Click the **"Enable Automatic Deploys"** button to make it possible for Heroku to rebuild the app a new change is pushed to GitHub repository.

 11. Click **"Deploy Branch"**.

