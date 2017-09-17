def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) <= 1 and char != aStr:
    	return False

    if char == aStr[len(aStr) // 2]:
    	return True
    elif ord(char) < ord(aStr[len(aStr) // 2]):
    	return isIn(char, aStr[0:len(aStr) // 2])
    else:
    	return isIn(char, aStr[len(aStr) // 2:])

print(isIn('v', 'abcdefghi'))