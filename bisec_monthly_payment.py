balance = 320000
annualInterestRate = 0.2

# Result should be : Lowest Payment: 29157.09

monthlyInterestRate = annualInterestRate / 12
lBound = balance / 12
uBound = (balance * (1 + monthlyInterestRate)**12) / 12
payment = (lBound + uBound) / 2
initBalance = balance

while True:
	initBalance = balance
	for x in range(12):
		initBalance -= payment
		initBalance += initBalance * monthlyInterestRate
	if initBalance <= 0.01 and initBalance > 0:
		break
	elif initBalance >= 0.01:
		lBound = payment
		payment = (lBound + uBound) / 2
	else:
		uBound = payment
		payment = (lBound + uBound) / 2

print("Lowest Payment: %.2f" % payment)