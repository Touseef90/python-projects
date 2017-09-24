def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    check = ''
    index = ''

    for x in aDict:
    	if len(aDict[x]) > len(check):
    		check = aDict[x]
    		index = x
    
    if len(index) != 0:
    	return index
    else:
    	return 'None'

print(biggest({}))