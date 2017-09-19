balance = 3329
annualInterestRate = 0.2

# Result should be - Lowest Payment: 310

monthlyInterestRate = 0.2 / 12
annualPayment = payment * 12

'''
for x in range(12):
	monthlyInterest = balance * monthlyInterestRate
	updatedBalance = balance + monthlyInterest

while annualPayment < updatedBalance:
	if annualPayment < updatedBalance:
		payment += 10
		annualPayment = payment * 12
'''

for x in range(12):
	payment = 10
	while balance - payment <= 0:
		payment += 10

print(updatedBalance)
print(payment)


'''
Monthly Unpaid		Updated Balance
3019 				3067.3
2757.3				2801.4
2491.4				2531.2
2221.2				2256.7
1946.7				1977.8
1667.8				1694.4
1384.4				1406.5
1096.5				1114
804					816.8
506.8				514.9
204.9				208.1
-101.9
3029				3077.4
2777.4				2821.8
2521.8				2562.1
2262.1				2298.2
1998.2				2030.1
1730.1				1757.7
1457.7				1481
1181				1199.8
899.8				914.2
614.2				624
324					329.1
29.1
'''
