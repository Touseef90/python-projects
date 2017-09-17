def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
    	return base / base
    else:
    	temp = 1
    	for x in range(exp):
    		temp *= base
    	return temp

print(iterPower(10, 2))
