def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
    	return base / base

    if exp == 1:
    	base / base
    	return base
    else:
    	return base * recurPower(base, exp-1)

print(recurPower(0.1, 0))
print(recurPower(4.16, 10))
print(recurPower(-6.18, 9))
print(recurPower(2, 3))

# Pata lagao ke neeche wala function ghalat kyu ha

def WrongFunctionRecurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
    	return base / base

    if exp == 1:
    	return base / base
    else:
    	return base * WrongFunctionRecurPower(base, exp-1)

print(WrongFunctionRecurPower(0.1, 0))
print(WrongFunctionRecurPower(4.16, 10))
print(WrongFunctionRecurPower(-6.18, 9))
print(WrongFunctionRecurPower(2, 3))