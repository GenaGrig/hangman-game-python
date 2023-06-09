import random
import time
import os


correctly_guessed_letters = []
'''
Global variable for correctly guessed letters
'''

incorrectly_guessed_letters = []
'''
Global variable for incorrectly guessed letters
'''

randomly_chosen_word = []
'''
Global variable for randomly chosen word
'''

player_lives = 6
'''
Global variable for lives left
'''

game_over = False
'''
Global variable for game over
'''

width = os.get_terminal_size().columns
'''
Determine width of terminal
'''


class text_colors:
    '''
    Class for text colors
    '''
    HEADER = '\033[95m'  # purple
    CYAN = '\033[96m'  # cyan
    BLUE = '\033[94m'  # blue
    GREEN = '\033[92m'  # green
    WARNING = '\033[93m'  # yellow
    WRONG = '\033[91m'  # red
    END = '\033[0m'  # white
    BOLD = '\033[1m'  # bold


def choose_random_word():
    '''
    Will choose a random word from the list of predefined words
    '''
    global randomly_chosen_word
    acceptable_words = []

    with open('countries.txt', 'r') as f:
        for line in f:
            acceptable_words.append(line.strip().lower())

    random.seed(time.time())
    randomly_chosen_word = random.choice(acceptable_words)


def draw_word():
    '''
    Will print the word with dashes instead of those letters
    that haven't been guessed yet
    '''
    global correctly_guessed_letters
    global randomly_chosen_word

    print(
        ' '.join(
            [
                letter if letter in correctly_guessed_letters
                else '_'
                if letter != ' '
                else ' '
                for letter in randomly_chosen_word
            ]
        )
    )
    print('\n')


def get_one_valid_letter():
    '''
    Validation for player input -
    entering only one letter at a time and no repeats
    '''
    is_letter_valid = False
    letter = ' '
    while is_letter_valid is False:
        letter = input('Enter guess letter: '.rjust(10//2))
        letter = letter.strip().lower()
        print('\n')
        if len(letter) <= 0 or len(letter) > 1:
            print(
                text_colors.WRONG
                + "You can type in only 1 letter at a time!\n"
                + text_colors.END
            )
        elif letter.isalpha():
            if (letter in correctly_guessed_letters
                or letter in incorrectly_guessed_letters
            ):  # noqa: E124
                print(
                    text_colors.WRONG
                    + "You already guessed letter"
                    + ' '
                    + text_colors.BOLD
                    + letter.upper()
                    + text_colors.END
                    + text_colors.WRONG
                    + ", try another one!\n"
                    + text_colors.END)
            else:
                is_letter_valid = True
        else:
            print(
                text_colors.WRONG
                + "You must enter a letter (a-z)!\n" + text_colors.END)

    return letter


def guess_letter():
    '''
    Will check if the letter is correct or wrong and update our global variable
    '''
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global randomly_chosen_word
    global player_lives
    global game_over

    letter = get_one_valid_letter()

    if letter in randomly_chosen_word:
        correctly_guessed_letters.append(letter)
        print(
            text_colors.GREEN
            + 'Correct! '
            + text_colors.BOLD
            + letter.upper()
            + text_colors.END
            + text_colors.GREEN
            + ' is in the country name!\n'
            + text_colors.END
        )
    else:
        incorrectly_guessed_letters.append(letter)
        # Sorts the list of incorrectly guessed letters alphabetically
        incorrectly_guessed_letters.sort()
        print(
            text_colors.WRONG
            + 'Wrong! '
            + text_colors.BOLD
            + letter.upper()
            + text_colors.END
            + text_colors.WRONG
            + ' is not in the country name!\n'
            + text_colors.END
        )
        print(text_colors.WRONG + "You lost a life!\n" + text_colors.END)
        print(
            text_colors.WARNING
            + "You have "
            + str(player_lives - 1)
            + " lives left!\n"
            + text_colors.END
        )
        player_lives -= 1


def check_for_game_over():
    '''
    Checks if player won or lost
    '''
    global game_over
    global player_lives
    global correctly_guessed_letters
    global randomly_chosen_word

    if player_lives == 0:
        game_over = True
        draw_hangman()
        print(
            text_colors.BOLD
            + text_colors.WRONG
            + 'You lost! The country name was '
            + randomly_chosen_word.upper()
            + ".\n Try to play again!\n"
            + text_colors.END
        )
        print(text_colors.WRONG + """
            __   __                _                        _ 
            \ \ / /               | |                      | |
             \ V /   ___   _   _  | |      ___   ___   ___ | |
              \ /   / _ \ | | | | | |     / _ \ / __| / _ \| |
              | |  | (_) || |_| | | |____| (_) |\__ \|  __/|_|
              \_/   \___/  \__,_| \_____/ \___/ |___/ \___|(_)
        """ + text_colors.END)
        restart_game()

    if len(correctly_guessed_letters) == len(
        set(randomly_chosen_word.replace(' ', ''))
    ):
        game_over = True
        print(
            text_colors.BOLD
            + text_colors.GREEN
            + 'Congratulations! You guessed the country name '
            + randomly_chosen_word.upper()
            + '!\n Try to guess another country!\n'
            + text_colors.END)
        print(text_colors.GREEN + """
            __   __                _    _  _         _ 
            \ \ / /               | |  | |(_)       | |
             \ V /   ___   _   _  | |  | | _  _ __  | |
              \ /   / _ \ | | | | | |/\| || || '_ \ | |
              | |  | (_) || |_| | \  /\  /| || | | ||_|
              \_/   \___/  \__,_|  \/  \/ |_||_| |_|(_)
            """ + text_colors.END)
        restart_game()


def restart_game():
    '''
    Restarts the game
    '''
    global player_lives
    global game_over
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global randomly_chosen_word

    player_lives = 6
    game_over = False
    correctly_guessed_letters = []
    incorrectly_guessed_letters = []
    randomly_chosen_word = ''

    while True:
        restart = input(
            text_colors.WARNING
            + 'Do you want to play again or go in menu? (yes/no/menu): '
            .rjust(10//2)
            + text_colors.END)
        print('\n')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            clear_screen()
            print('Good luck! Try to guess country name in 6 attempts!\n')
            choose_random_word()
            break
        elif restart.lower() == 'no' or restart.lower() == 'n':
            print(text_colors.GREEN +
                  'Thanks for playing! See you next time!' + text_colors.END)
            exit()
        elif restart.lower() == 'menu' or restart.lower() == 'm':
            clear_screen()
            execfile(filename='run.py')
        else:
            print(text_colors.WRONG + 'Please enter y or n!' + text_colors.END)


def execfile(filename, globals=None, locals=None):
    '''
    This function is used to run the code in a file
    as if it were in the main module.
    It is used to run the code in the run.py file.
    '''
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filename,
        "__name__": "__main__",
    })
    with open(filename, 'rb') as file:
        exec(compile(file.read(), filename, 'exec'), globals, locals)


def clear_screen():
    '''
    Clears the screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_hangman():
    '''
    Will draw our hangman based on the lives left.
    '''
    global player_lives

    if player_lives == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+\n")
    elif player_lives == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+\n")
    elif player_lives == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif player_lives == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+\n")
    elif player_lives == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+\n")
    elif player_lives == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+\n")
    elif player_lives == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+\n")


def main():
    '''
    Main functions of application and entry point of the game
    '''
    global game_over

    clear_screen()
    print('\n')
    print("------ Welcome to Hangman Country Quiz ------\n".center(width))
    name = input('Enter your name: '.rjust(90//2))
    print('\n')
    print('Welcome' + text_colors.WARNING + ' ' + name + text_colors.END +
          '! Try to guess country name in 6 attempts!\n')
    choose_random_word()

    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print(text_colors.WARNING + 'Incorrect guesses:' + text_colors.END)
            print(incorrectly_guessed_letters)
            print('\n')

        guess_letter()
        check_for_game_over()


if __name__ == '__main__':
    main()
