import random
import time

'''
HANGMAN GAME

How it will work:
1. A random word will be chosen from our list of words.
2. The player will have 6 lives to guess the all letters, otherwise player looses.
3. The player can guess only one letter at a time.
4. Before every guess player can see previous guesses.
5. Before every guess our hangman drawing will be displayed based on the number of lives left.
6. If all letters are guessed right before all lives are over, a win message will display.
7. If all lives are over, a loose message will display
'''

# Global variable for correctly guessed letters
correctly_guessed_letters = []

# Gloval variable for incorrectly guessed letters
incorrectly_guessed_letters = []

# Global variable for randomly chosen word
randomly_chosen_word = ''

# Global variable for lives left
player_lives = 6

# Global variable for game over
game_over = False

class text_colors:
    '''
    Class for text colors
    '''
    HEADER = '\033[95m' # purple
    BLUE = '\033[94m' # blue
    GREEN = '\033[92m' # green
    WARNING = '\033[93m' # yellow
    WRONG = '\033[91m' # red
    END = '\033[0m' # white
    BOLD = '\033[1m' # bold
    UNDERLINE = '\033[4m' # underline

# 7 different methods to run the game and processes

def choose_random_word():
    '''
    Will choose a random word from the list of predefined words
    '''
    global randomly_chosen_word
    acceptable_words = []

    with open('words.txt', 'r') as f:
        for line in f:
            acceptable_words.append(line.strip().lower())

    random.seed(time.time())
    randomly_chosen_word = random.choice(acceptable_words)

def draw_word():
    '''
    Will print the word with dashes instead of those letters that haven't been guessed yet
    '''
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter = randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print('')

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
    
def get_one_valid_letter():
    '''
    Some sort of validation for player entering only one letter at a time with no repeats
    '''
    is_letter_valid = False
    letter = ''
    while is_letter_valid is False:
        letter = input('Enter guess letter: \n')
        letter = letter.strip().lower()
        if len(letter) <=0 or len(letter) >1:
            print(text_colors.WRONG + "You can type in only 1 letter at a time!\n" + text_colors.END)
        elif letter.isalpha():
            if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:
                print(text_colors.WRONG + "You already guessed letter" + ' ' + text_colors.BOLD + letter.upper() 
                + text_colors.END + text_colors.WRONG + ", try another one!\n" + text_colors.END)
            else:
                is_letter_valid = True
        else:
            print(text_colors.WRONG + "You must enter a letter (a-z)!\n" + text_colors.END)

    return letter

def guess_letter():
    '''
    Will check if the letter is correct or wrong and update our global variable
    '''
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global player_lives

    letter = get_one_valid_letter()
    if letter in randomly_chosen_word:
        correctly_guessed_letters.append(letter)
    else:
        incorrectly_guessed_letters.append(letter)
        player_lives -= 1

def check_for_game_over():
    '''
    Checks if player won or lost
    '''
    global player_lives
    global game_over
    global correctly_guessed_letters

    if player_lives <= 0:
        game_over = True
        draw_hangman()
        print(text_colors.BOLD + text_colors.WRONG + 'You lost! The sport was ' + randomly_chosen_word.upper() + ". Try to play again!" + text_colors.END)
    else: 
        guessed_all_letters = True
        for letter in randomly_chosen_word:
            if letter not in correctly_guessed_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            game_over = True
            print(text_colors.BOLD + text_colors.GREEN + 'Congratulations! You guessed the sports name ' + randomly_chosen_word.upper() 
            + '! Try to guess another sport type!' + text_colors.END)


def main():
    '''
    Main functions of application and entry point of the game
    '''
    global game_over

    print("------ Welcome to Hangman Sports Quiz ------\n")
    name = input('Enter your name: \n')
    print(f'Welcome {name}! Try to guess sport name in 6 attempts!')
    choose_random_word()

    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print('Incorrect guesses:')
            print(incorrectly_guessed_letters)

        guess_letter()
        check_for_game_over()

if __name__ == '__main__':
    while True:
        print('(P) Play Hangman sports game')
        print('(Q) Quit')
        choice = input('Enter your choice: ').lower()
        if choice == 'p':
            main()
        elif choice == 'q':
            exit()
        else:
            print(f'Not a correct choice: {choice}')