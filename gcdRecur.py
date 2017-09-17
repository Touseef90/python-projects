def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a % b == 0:
    	return b
    else:
    	return gcdRecur(a, a % b)

print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))

def BothWork_gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
    	return a
    else:
    	return BothWork_gcdRecur(b, a % b)

print(BothWork_gcdRecur(90, 375)) # 15
print(BothWork_gcdRecur(63, 84)) # 21
print(BothWork_gcdRecur(238, 322)) # 14
print(BothWork_gcdRecur(96, 84)) # 12
