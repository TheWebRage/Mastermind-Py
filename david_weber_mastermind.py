# Mastermind
# David Weber
# WEB 3200
# 9/14/2020

import random


def get_computer_choice():
    random_selection = list()
    for i in range(0, 4):
        random_selection.append(random.choice(allOptions))
    return random_selection


def get_hint(user_guess, computer_choice):
    hint_to_return = ['#', '#', '#', '#']

    for i in range(0, len(user_guess)):
        if user_guess[i] == computer_choice[i]:
            computer_choice[i] = '.'
            user_guess[i] = '.'
            hint_to_return[i] = '*'

    for i in range(0, len(user_guess)):
        for j in range(0, len(computer_choice)):
            if user_guess[i] == computer_choice[j] and computer_choice[j] != '.':
                computer_choice[j] = '.'
                user_guess[i] = '.'
                hint_to_return[i] = '~'

    str = ''
    return str.join(hint_to_return)


def interact_with_user(computerChoice):
    print('The code to guess: ' + str(computerChoice))
    userGuess = input('\nWhat is your guess? (Choose from R G B Y W P -- For example you could enter RGBY or YYYY) ')
    userGuess = list(userGuess.upper())
    print('\nYour guess: ' + str(userGuess))

    hint = get_hint(userGuess[:], computerChoice[:])

    print('Your clue: ' + hint)
    print("'*' = correct color guess in correct location,")
    print("'~' = correct color guess in WRONG location,")
    print("'#' = guess is wrong color in wrong location\n")
    return hint


def print_number_of_guesses(numberOfGuesses):
    if numberOfGuesses == 1:
        print('Good job! You got it on your first guess!')
    else:
        print('Good job! It took you ' + str(numberOfGuesses) + ' guesses.')


# Start Game Logic

print('MasterMind')

allOptions = ['R', 'G', 'B', 'Y', 'W', 'P']
numberOfGuesses = 0
endgame = False

while not endgame:

    if numberOfGuesses == 0:
        computerChoice = get_computer_choice()

    numberOfGuesses += 1

    hint = interact_with_user(computerChoice)

    if hint == '****':
        endgame = True
        print_number_of_guesses(numberOfGuesses)

        playAgain = input('Do you want to play again? (Y/N) ')
        if playAgain.upper() == 'N':
            break
        else:
            numberOfGuesses = 0
            endgame = False

print('\nThanks for playing Mastermind!')
