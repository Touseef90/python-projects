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
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):

    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for x in range(len(secretWord)):
        if secretWord[x] in lettersGuessed:
            count += 1
    return count == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    char = ''
    for x in range(len(secretWord)):
        if secretWord[x] in lettersGuessed:
            char += secretWord[x]
        else:
            char += '_'
    return char

def getAvailableLetters(lettersGuessed):
    alpha = ''
    for x in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[x] in lettersGuessed:
            pass
        else:
            alpha += string.ascii_lowercase[x]
    return alpha

def hangman(secretWord):

    noOfGuess = 8
    alpha = string.ascii_lowercase
    guessed = []
    guess = ''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord) ,'letters long.')
    print('-------------')

    while noOfGuess:
        print('You have', noOfGuess ,'guesses left.')
        print('Available letters: '+ alpha)
        guess = input('Please guess a letter: ')
        # print(guess)

        guessed = getGuessedWord(secretWord, guess)

        if guess in guessed:
            print("Oops! You've already guessed that letter: "+ guessed)
            noOfGuess -= 1
        elif guess in guessed:
            guessed = guess
            noOfGuess -= 1
            print('Good guess: '+ guessed)
        else:
            print('Oops! That letter is not in my word: '+ guessed)
            noOfGuess -= 1

        if isWordGuessed(secretWord, guessed):
            print('Good guess: '+ secretWord)
            print('-------------')
            print('Congratulations, you won!')
            return secretWord

hangman('hello')
