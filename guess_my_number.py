low = 0
high = 100
ans = (low + high) // 2
reply = ''

print('Please think of a number between 0 and 100!')

while reply != 'c':
	print('Is your secret number ' + str(ans) + '?')

	reply = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

	if reply == 'c':
		print('Game over. Your secret number was: ' + str(ans))
		break
	elif reply == 'h':
		high = ans
		ans = (low + high) // 2
	elif reply == 'l':
		low = ans
		ans = (low + high) // 2
	else:
		print('Sorry, I did not understand your input.')
