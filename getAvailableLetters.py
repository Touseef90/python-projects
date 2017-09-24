import string

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

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getAvailableLetters(lettersGuessed))