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

### 3. Start of the game. First screen.

* Personalized welcome message with player name.
* Hangman drawing
* Word is shown with underscores (_ _ _ _ _) instead of letters.
* Implemented several word guesses with spaces between them
* "Enter guess letter:" player input string

First game screen, after input player name, shows a personalized player welcome message with player name colored in yellow. Then the gallows itself draws. We see only the default structure with a small piece of a rope. Below that word is shown with underscores instead of letters. In this example there is a space between the underscores, which means that there are two words to guess. There can be three or four words to guess and all of them are divided with space. 

![First game move](/pic/first_game_move.PNG)

### 4. The Game

* Correct guess
    * Correctly guessed letter is shown in the word instead of uderscore on a correct place
    * Green colored message with correctly guessed letter is shown to player

When the guess is correct, green string is showing it, saying "Correct! Letter (correct guessed letter) is in the word (name of the topic).

![Correct guess of the letter](/pic/correct_guess.PNG)

* Incorrect guess
    * Incorrect letter shows in red colored message
    * Lose a life message is shown in red color
    * How many lives left shows in yellow color (default lives amount is 6)
    * Gallows is drawn and a hangmans head is drawn as a first part of a body
    * Incorrect guesses list shows upp with incorrect letters in it
    * Spaces are added between lines to make readability easier

![Incorrect guess of the letter](/pic/incorrect_guess.PNG)

### 5. Player input validation

* There are three levels of player input validation
    * Repeated guesses
    * More than 1 letter inputs
    * Other than letters symbols and numbers

This is important part of the game as it can disturb the player experience if this wrong inputs will not be fixed. 
Already guessed letters are validating and as a result player will see a red colored message which will say that this letter player already guessed, which means that letter is in correctly or incorrectly guessed letters list (in first case it will be shown in the word itself). 
Multiple inputs is also validating and if player will input more than 1 letter, a red colored message will show up saying that player can type in only one letter at a time.
The last validation is called letter.isalpha or by simple words it must be a letter, not a symbol or number. In case user will type in number or any other symbol like *%&#, a red colored message will show up saying that player must enter a letter from a to z (it does not matter upper or lowercase).

![Player input validations](/pic/input_validations.PNG)

### 6. Winning the game

* Player will see the last correct guessed letter in the word in green color
* Congratulations message with the full correct guessed word in green color
* You win! graphics in green color
* Question if player wants to play again or go in menu (third alternative is quit if none of previuos choices will be made) in yellow color
* Player can type in full words "yes/no/menu" or only first letters "y/n/m"

The last screen if player wins the game shows congratulations message with the gueesed word or words, big graphics You Win! and a question about wish to play again or return to main menu. If player will type in "no or n" game will be terminated. 
The green color is added to congratulations message and graphics to make it more attractive. The yellow color is added for play again question as a waiting of user choice. 

![You win final screen](/pic/you_win_screen.PNG)

### 7. Loosing the game

* Player will see a message with zero lives left in yellow color
* Player will see a gallows with hangman
* Red colored message saying that player lost the game and the correct word or words will show up in red color.
* You Lose! graphics in red color will show up
* Question if player wants to play again or go in menu (third alternative is quit if none of previuos choices will be made) in yellow color
* Player can type in full words "yes/no/menu" or only first letters "y/n/m"

As in the winning screen on the loosing screen will be displayed same information with some differences in color - from green it is red now. But the correct word(s) is displayed as well as the question of playing again.

![You lost final screen](/pic/you_lost_screen.PNG)

### 8. Game restart

If player types in "yes or y" to restart:

* Good luck message!
* Gallows default structure
* Word with underscores
* "Enter guess letter:" player input
* Clear screen function is used to clear the interpreter screen from previous game

![Restarted game screen](/pic/restarted_game.PNG)

If player types in "menu or m" to enter menu

* Player goes back to welcome screen with main menu
* Clear screen function works and clears the interpreter from previous game showing welcome screen and main menu

If player types in "no or n"

* Player sees a message in green color saying "Thanks for playing! See you next time!"
* If Quit option was chosen from main menu "Thank you for playing!" will show up in yellow color.

![Choice 'no' from restart the game question](/pic/quit_the_game1.PNG)

![Choice 'quit' from main menu](/pic/quit_the_game2.PNG)

# Future features

* High scores or leaderboard. This feature can show high scores of the players, counting correctly or incorrectly guessed words and applying scoring to them based on the scale in the end of the game, when player will quit.

* Difficulty settings. Possible feature, because features implemented right now do not allow to choose difficulty or make a categories that can be base for it. Amount of 6 attempts is challenging, but research showed that chance to win or lose is 50% despite of length of the word. 

* Option to enter the whole word instead of guessing by one letter at a time. In this case, validation method should be changed, because now it does not allow to enter more than one letter at once.

# Technologies used

## Languages

* Python

## Other programs and websites

* [Lucidchart](https://www.lucidchart.com/pages/) for creating flowchart and diagrams
* [Heroku](www.heroku.com) for deploying the game online
* [GitHub](www.github.com) for storing project repository
* [Visual Studio Code](https://code.visualstudio.com/) for coding the game and pushing it to GitHub

* Python modules
    * random - to choose random word from the list
    * time - to make random words not to be chosen again in a certain limit of time to avoid repeats of guessed words
    * os - module to work with operating systems

# Testing

| Feature | Description | Action | Result |
| -------|--------|--------|--------|
| Welcome screen | Graphics display | N/A | Shows correctly |
| Main menu | Choices of topics, game rules and quit | N/A | Shows correctly
| Player choice input | Input string and cursor active | Type in | Types numbers and letters
| Option 1 | Hangman sports | 1 & Enter | Works correctly |
| Option 2 | Hangman Movies | 2 & Enter | Works correctly |
| Option 3 | Hangman Countries | 3 & Enter | Works correctly |
| Option 4 | Game rules | R & Enter | Works correctly |
| Option 5 | Quit | Q & Enter | Works correctly |
| Name input | after choice 1,2,3 & Enter | 1,2 or 3 & Enter| Works correctly
| Game screen 1 | Welcome message with name| N/A | Shows correctly 
| Game screen 1 | Gallows drawn | N/A | Shows correctly
| Game screen 1 | Word shown as underscores | N/A | Shows correctly
| Game screen 1 | Player input for a letter | letter + Enter | Works correctly
| Input validation | Repetitions, multiple inputs, not a letter | N/A | Works correctly
| Game screen 2 | Correct guess message | N/A | Shows correctly
| Game screen 2 | Underscores substitutes by correctly guessed letters | N/A | Shows correctly
| Game screen 2 | Incorrect guess message | N/A | Shows correctly
| Game screen 2 | Lost a life message | N/A | Shows correctly
| Game screen 2 | Lives left message | N/A | Shows correctly
| Game screen 2 | Gallows with hangman | N/A | Shows correctly
| Game screen 2 | Incorrect guesses list | N/A | Shows correctly
| Game screen 2 | Validation messages on incorrect inputs | N/A | Shows correctly
| Game screen 3 | Updated lives left message | N/A | Shows correctly
| Game screen 3 | Gallows with hangman new body part (incorrect guess) | N/A | Shows correctly
| Game Win screen| Congratulations message | N/A | Shows correctly
| Game Win screen | Sports (or other topics) name | N/A | Shows correctly
| Game Win screen | You Win graphics | N/A | Shows correctly
| Game Win Screen | Play again question and options | yes/no/menu or y/n/m $ Enter | Shows correctly
| Game Win Screen | Restart the game | yes or y & Enter | Works correctly
| Game Win Screen | Quit the game | no or n & Enter | Works correctly
| Game Win Screen | Return to menu | menu or m & Enter | Works correctly
| Clear screen | Clears the screen from previous game after restart or return to menu | N/A | Works correctly
| Game Lost screen| Zero lives message | N/A | Shows correctly
| Game Lost screen| Gallows with full body of hangman | N/A | Shows correctly
| Game Lost screen| You lost message | N/A | Shows correctly
| Game Lost screen | Correct sports (or other topics) name | N/A | Shows correctly
| Game Lost screen | You Lose graphics | N/A | Shows correctly
| Game Lost Screen | Play again question and options | yes/no/menu or y/n/m $ Enter | Shows correctly
| Game Lost Screen | Restart the game | yes or y & Enter | Works correctly
| Game Lost Screen | Quit the game | no or n & Enter | Works correctly
| Game Lost Screen | Return to menu | menu or m & Enter | Works correctly
| Clear screen | Clears the screen from previous game after restart or return to menu | N/A | Works correctly
| Game overall | Colors in game - cyan, red, yellow, green | N/A | Shows correctly
| Game overall | Thank you message when quitting the game | N/A | Shows correctly
| Game overall | Program is terminated after quit | Q & Enter, no or n & Enter | Works correctly

# Bugs 

* Input bug on different mobile devices and tablets
    * When trying to type in letter, device adds numbers or previous letters (tested on Samsung Galaxy 9 and Lenovo tablet). 
    * Testing on Nokia 7+ was successful and no bugs were detected.

# Validation

### Lighthouse desktop

* SEO is 89 because no meta information is in code

![Lighthouse desktop performance](/pic/lighthouse.PNG)

### Lighthouse mobile

![Lighthouse mobile performance](/pic/lighthouse_mobile.PNG)

## CI Python Linter

* Known warning
    * Invalid escape sequence (this is used for creating the graphics and it has a lot of whitespaces)

![Python validation results](/pic/python_validation.PNG)

# Testing user stories

* As a first time visitor, I want to see a name and understandable navigation of the game
    * Main menu and other activities, that needs player desicions and input are made in a clear and understandable way. All the navigation in the game is intuitive and easy to follow by typing in appropriate letters.
* As a first time visitor, I want to be able to read the rules of the game
    * For those who play the game for the first time, there is a short game rules, accesseble from the main menu by pressing Q and Enter.
* As a first time visitor, I want to select difficulty or interesting topic of the game
    * Right now the difficulty of the game is not implemented, instead of this, player can choose one of three topics or interested theme, from which random word will be chosen. There are both short and long words, in movies and countries two or more words to guess at once are presented. Player has only 6 attempts to guess the word, and this is fair challenge with even chances to win or lose.
* As a first time visitor, I want to get feedback on my actions in the game
    * Each action in the game is supported by messages. If player makes wrong choice or input, player will be informed about it and given a chance to try again. Game will accept only correct input according to where player is, in menu, the game or restart the game choice. During the game player will see messages about correct or incorrect choice and win or lose statement in the end of the game, with a question about restart, quit or return to main menu.
* As a first time visitor, I do not want to meet bugs, that will disturb my game experience
    * No bugs were detected during testing of the game. Everything works as it should.
* As a first time visitor, I want to meet a challenge in playing the game
    * The game makes a challenge by letting a player guess the word in only 6 attempts despite of the length. It can be a short word of 4-5 letter, long word or even more than one word to guess. Chance to win or lose is 50%. In future features can be implemented more understandanle difficulty scale, but rigth now it is set to medium level.

# Deployment

## Deploying

1. Go to the Heroku Dashboard.
2. Click New in right upper corner.
3. Select to create a new app.
4. Enter new app name and click "Create app"
5. Add Config Var's for Creds and Port if needed.
6. Set the buildbacks to Python and NodeJS in that order.
7. Link the Heroku app to the GitHub repository.
8. Click on Deploy.
9. View your app in terminal. [My hangman game on Heroku](https://sports-hangman.herokuapp.com/)

## Creating a fork
1. Navigate to the [repository](https://github.com/GenaGrig/hangman-game-python.git)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description.
4. Choose to copy only the main branch or all branches to the new fork.
5. Click Create a Fork. A repository should appear in your GitHub.

## Cloning a repository
1. Navigate to the [repository](https://github.com/GenaGrig/hangman-game-python.git)
2. Click on the Code button on top of the repository and copy the link.
3. Open Git Bash and change the working directory to the location where you want the cloned directory.
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

# Credits

## Content

* README file was written with help of following documents:
    * Code Institute [README template](https://github.com/Code-Institute-Solutions/readme-template)
    * GitHubs [Basic writing and formatting syntax](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings)
    * Hints and some structure of README files from existing projects from other CI students
* Main idea of the game and Python code basics were taken by code along with this video from [CS Students channel](https://youtu.be/ynwB-QfOPRw)
* Some of code function was written with help of [GitHub Copilot](https://github.com/features/copilot)
* Colors for text and graphics was taken from the answer in this topic on [stackoverflow.com](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal) 
* Centering strings in python [How to use center() function?](https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/center/python-string-center/#:~:text=To%20center%20align%20a%20text,it%20with%20a%20specified%20character.)
* Aligning text and input cursor methods was taken from [this website](https://www.tutorialspoint.com/how-to-align-text-strings-using-python#:~:text=By%20specifying%20the%20alignment%20as,followed%20by%20the%20width%20number.)
* Text to ASCII Art Generator (TAAG)[Link](http://patorjk.com/software/taag/#p=display&h=0&f=Acrobatic&t=Type%20Something%20)
* Python Formatter and Beautifier [Link](https://codebeautify.org/python-formatter-beautifier#)

# Acknowledgements

* I want to thank my mentor Maranatha Ilesanmi for very good feedback and very useful advices that made my project complete and interesting. Very good ideas from my mentor that was implemented and made project look more solid.
* I want to thank members on our Slack community for giving feedback and showing their own projects that was inspiring in different ways.



