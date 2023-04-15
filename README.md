# Hangman word guessing game

Hangman is a classical word guessing game, where player try to guess a random word chosen by AI from the predefined list of words. Player has a limited amount of attempts and each time player guesses wrong letter, number of attempts decreases and program draws a hangman part of a body. If the player loses the game, graphics will draw a man hanged on the gallows, if player wins, restart of the game, quitting or return to menu are the options to choose. 

In this version of Hangman, I implemented topics, which player can choose from and guess the words based on them. Instead of guessing a random word, player can choose to guess a sports, movie or a country name. Game can be expandable and more topics can be added.

Game is written on Python and deployed to Heroku, where everyone can play it.  

[Link to Hangman game on Heroku](https://sports-hangman.herokuapp.com/)

[Link to a GitHub repository](https://github.com/GenaGrig/hangman-game-python.git)

![Screenshot of Hangman's main menu](/pic/main_menu.PNG)

# How to play

1. Player chooses a topic to play, in which word will be chosen (Sports, Movies or Countries)
    * a. Player can read the rules of the game
    * b. Player can quit the game
2. Player enter his name
3. Player guesses letters, one at a time
    * a. Input validation is used every time player inputs the letter
        * No repeats of already guessed correct or incorrect letters
        * No inputs of more than 1 letter at once
        * No inputs of other symbols or numbers, only letters a-z 
4. If player guesses all letters in less than 6 attempts - player wins, otherwise player looses.
5. Player chooses to restart the game in the same topic, go to main menu or quit the game.

# User experience

## User stories

### First time visitor goals

* As a first time visitor, I want to see a name and understandable navigation of the game
* As a first time visitor, I want to be able to read the rules of the game
* As a first time visitor, I want to select difficulty or interesting topic of the game
* As a first time visitor, I want to get feedback on my actions in the game
* As a first time visitor, I do not want to meet bugs, that will disturb my game experience
* As a first time visitor, I want to meet a challenge in playing the game

# Planning Flowchart

Before the game coding, I made a structure of the game in a flowchart, to understand:
* What choices will main menu have?
* How validation of wrong choices in main menu will work?
* What validations needed to prevent repetitions or wrong inputs from player when guessing the letters?
* What are results in guessing letter wright or wrong?
* What are results in guessing all letters wright or wrong in limited amount of attempts?
* What next after winning or loosing the game?

![Flowchart of the Hangman game](/pic/Flowchart_Hangman.png)

# Design and features of the game

## Existing features

### 1. Welcome screen - main menu

* Hangman graphics in cyan color
* Three game topic choices to play
* Read the rules option
* Quit option
* "Enter your choice:" player input string

Both Hangman graphics and menu is centered, to make the game welcome screen more attractive and have a feeling of first games in 90's with manual input of choices and some simple graphics.

![Welcome screen and main menu](/pic/welcome_screen.PNG)

### 2. Name screen

* Welcome message with name of the topic chosen by player
* "Enter your name:" player input string

This adds some attractiveness and will show in next window personalised welcome message to player. Both welcome message and player input string are centered for better look.

![Enter player name string](/pic/enter_name.PNG)

3. Start of the game. First screen.
* Personalized welcome message with player name.
* Hangman drawing
* Word is shown with underscores (_ _ _ _ _) instead of letters.
* Implemented several word guesses with spaces between them
* "Enter guess letter:" player input string

First game screen, after input player name, shows a personalized player welcome message with player name colored in yellow. Then the hangman itself draws, we see only the default structure with a small piece of a rope. 