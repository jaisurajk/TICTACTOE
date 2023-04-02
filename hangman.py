# assignment: programming assignment 1
# author: Jaisuraj Kaleeswaran
# date: 2023-03-09
# file: hangman.py is a program that plays the hangman game.
# input: Fist, the input is the file 'dictionary.txt'. Then, the user inputs are the size of the word being guessed, the number of lives, and letters the user will guess to find the right word that fits the size inputed.
# output: The outputs are the hangman game, the letters guessed, the display of the number of lives, and the correct word.

from random import choice, randint

# make a dictionary.txt in the same folder where hangman.py is located
dictionary_file = "dictionary.txt"

# write all your functions herediff -wB output3 ex3.out

def game_structure(attempts, word, lives):
    print("Letters chosen:", ", ".join(attempts))
    letters = []
    for i in word:
        if i == "-" or i in attempts:
            letters.append(i)
        else:
            letters.append("__")
    print(f'{"  ".join(letters)}   lives: {lives} {(health-lives) * "X"}{lives * "O"}')

def choose(attempts):
    l = input("Please choose a new letter >\n").upper()
    if not (l.isalpha() and len(l) == 1):
        l = choose(attempts)
    elif l in attempts:
        print("You have already chosen this letter.")
        l = choose(attempts)
    else:
        return l
    return l

def game_on(attempts, word, lives):
    game_structure(attempts, word, lives)
    if lives >= 1:
        for i in word:
            if not (i == "-" or i in attempts):
                return True
        print(f"Congratulations!!! You won! The word is {word}!")
    else:
        print(f"You lost! The word is {word}!")
    return False

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary(filename):
    dictionary = {}
    max_size = 12
    try:
        f = open(filename, "r")
        for i in f:
            i = i.strip()
            if max_size <= len(i):
                dictionary.setdefault(max_size, []).append(i)
            else:
                dictionary.setdefault(len(i), []).append(i)       
        f.close()
    except FileNotFoundError:
        print(f"The program will stop running as the file {filename} does not exist.")
        exit()
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary(dictionary):
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    try:
        size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]: \n"))
        if 3 <= size <= 12:
            print(f"The word size is set to {size}.")
        else:
            raise Exception
    except Exception:
        size = randint(3, 12)
        print("A dictionary word of any size will be chosen.")
    try:
        lives = int(input("Please choose a number of lives [1 - 10, default 5]: \n"))
        if 1 <= lives <= 10:
            print(f"You have {lives} lives.")
        else:
            raise Exception
    except Exception:
        lives = 5
        print(f"You have {lives} lives.")
    return (size, lives)


# MAIN

if __name__ == '__main__':

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary

    # print_dictionary(dictionary)

    # print a game introduction

    print("Welcome to the Hangman Game!")

 # START MAIN LOOP (OUTER PROGRAM LOOP)

    while True:

     # set up game options (the word size and number of lives)
        len_word, lives = get_game_options()
        attempts = []
        health = lives
        
    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)

        word = choice(dictionary[len_word]).upper()
        # word = "T-SHIRT"
        # print(word)

    # START GAME LOOP   (INNER PROGRAM LOOP)

        while True:
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            game_structure(attempts, word, lives)
            
            # ask the user to guess a letter
            l = choose(attempts)
            
    # update the list of chosen letters
            attempts.append(l)
            
    # if the letter is correct update the hidden word,
    # else update the number of lives
    # and print interactive messages
            if l in word:
                print("You guessed right!")
            else:
                lives -= 1
                print("You guessed wrong, you lost one life.")
                
    # END GAME LOOP   (INNER PROGRAM LOOP)
    # check if the user guesses the word correctly or lost all lives,
    # if yes finish the game
            if not game_on(attempts, word, lives):
                break
            
    # END MAIN LOOP (OUTER PROGRAM LOOP)
        play = input("Would you like to play again [Y/N]?\n").upper()
        if play == "Y":
            continue
        else:
            print("Goodbye!")
            exit()

    # ask if the user wants to continue playing,
    # if yes start a new game, otherwise terminate the program
