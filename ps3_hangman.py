# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    count = 0
    for x in range(len(secretWord)):
        if secretWord[x] in lettersGuessed:
            count += 1
    return count == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    char = ''
    for x in range(len(secretWord)):
        if secretWord[x] in lettersGuessed:
            char += secretWord[x]
        else:
            char += '_'
    return char



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = ''
    for x in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[x] in lettersGuessed:
            pass
        else:
            alpha += string.ascii_lowercase[x]
    return alpha
    

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
    noOfGuess = 8
    alpha = string.ascii_lowercase
    lettersGuessed = []
    guess = ''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    while noOfGuess:
        print('You have', noOfGuess, 'guesses left.')
        print('Available letters: ' + alpha)
        guess = input('Please guess a letter: ')

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if isWordGuessed(secretWord, lettersGuessed):
                print('Good guess: ' + secretWord)
                print('-------------')
                print('Congratulations, you won!')
                noOfGuess = 0
            else:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                alpha = alpha.replace(guess, "")
        elif guess in alpha:
            alpha = alpha.replace(guess, "")
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            noOfGuess -= 1
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
    if isWordGuessed(secretWord, lettersGuessed):
        pass
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
