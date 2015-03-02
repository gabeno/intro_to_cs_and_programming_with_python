# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

'''
Requirements
============

Here are the requirements for your game:

1. The computer must select a word at random from the list of available words
   that was provided in words.txt. The functions for loading the word list
   and selecting a random word have already been provided for you in ps3_hangman.py.

2. The game must be interactive; the flow of the game should go as follows:

   - At the start of the game, let the user know how many letters the computer's
    word contains.
   - Ask the user to supply one guess (i.e. letter) per round.
   - The user should receive feedback immediately after each guess about
    whether their guess appears in the computer's word.
   - After each round, you should also display to the user the partially
    guessed word so far, as well as letters that the user has not yet guessed.

3. Some additional rules of the game:

   - A user is allowed 8 guesses. Make sure to remind the user of how many
   guesses s/he has left after each round. Assume that players will only ever
   submit one character at a time (A-Z).
   - A user loses a guess only when s/he guesses incorrectly.
   - If the user guesses the same letter twice, do not take away a guess - instead,
   print a message letting them know they've already guessed that letter and ask
   them to try again.
   - The game should end when the user constructs the full word or runs out of
   guesses. If the player runs out of guesses (s/he "loses"), reveal the word
   to the user when the game ends.
'''

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    iter_bool = []
    for ltr in secretWord:
        iter_bool.append(ltr in lettersGuessed)
    return all(iter_bool)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = ''
    for ltr in secretWord:
        if ltr in lettersGuessed:
            guessedWord += ltr
        else:
            guessedWord += '_ '
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string

    available_letters = ''
    for ltr in string.ascii_lowercase:
        if ltr not in lettersGuessed:
            available_letters += ltr

    return available_letters


def separator():
    print '-'*13


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    guesses = 8

    game_up = False

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long.' % len(secretWord)
    print '-'*13

    while not game_up:
        print 'You have %s guesses left.' % guesses
        print 'Available letters: %s' % getAvailableLetters(lettersGuessed)
        letterGuessed = raw_input('Please guess a letter: ')
        letterGuessed = letterGuessed.lower()

        if letterGuessed:
            if letterGuessed in lettersGuessed and letterGuessed:
                print 'Oops! You\'ve already guessed that letter: %s' % getGuessedWord(secretWord, lettersGuessed)
                print '-'*13
            else:
                lettersGuessed.append(letterGuessed)

                # check if letter in secret word
                if letterGuessed not in secretWord:
                    print 'Oops! That letter is not in my word: %s' % getGuessedWord(secretWord, lettersGuessed)
                    guesses -= 1
                else:
                    print 'Good guess: %s' % getGuessedWord(secretWord, lettersGuessed)
                print '-'*13

                # guesses depleted?
                if guesses < 1 and not isWordGuessed(secretWord, lettersGuessed):
                    print 'Sorry, you ran out of guesses. The word was %s.' % secretWord
                    game_up = True

                # correct guess
                if isWordGuessed(secretWord, lettersGuessed):
                    print 'Congratulations, you won!'
                    game_up = True


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
hangman('tact')
