def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
    	m = a
    else:
    	m = b

    while m > 1:
    	if a % m == 0 and b % m == 0:
    		return m
    	else:
    		m -= 1
    return m

print(gcdIter(15, 5))