import math

def polysum(n, s):
	'''
	n, s: int or float and >= 0

	returns: sum of area and square of perimeter
	'''
	area = (0.25 * n * s**2) / math.tan(math.pi / n)
	perimeter = (s * n)**2
	return round(area + perimeter, 4)
