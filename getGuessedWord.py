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

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getGuessedWord(secretWord, lettersGuessed))