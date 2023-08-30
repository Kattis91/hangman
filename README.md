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

 Flowchart was created using [Lucidchart]("https://www.lucidchart.com/pages/sv")

 ![image](readme-images/flowchart.jpeg)

 ## Features 

 ### Welcome message

 ![image](readme-images/welcoming-message.jpg)
  
  - Tells a player what type of game it is.
  
  - Gives information about the game, amount of attempts, and the possibility to play several times.

  - Requests player's name.

### Name Validation

#### Input validation and error-checking:

![image](readme-images/no-whitespaces-in-name.jpg)

  - It is not possible to enter only spaces.

  - A player will get an error message.

  - The error message will continue to display until the player enters a valid name or an empty word. The error message for empty words is shown in the image below.
   
![image](readme-images/no-empty-strings-in-name.jpg)

  -  It is not possible to enter an empty word as a name.

  -  A player will get an error message.

  - The error message will continue to display until the player enters a valid name or only whitespaces. The error message for whitespaces is shown in the first image in this section.

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

      ![image](readme-images/letter-is-in-the-word.png)

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

