def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for x in aDict:
    	count += len(aDict[x])
    return count

print(how_many({'B': [15], 'u': [10, 15, 5, 2, 6]}))