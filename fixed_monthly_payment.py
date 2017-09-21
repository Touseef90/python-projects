balance = 3227
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
init_balance = balance
monthlyPayment = 0

while init_balance > 0:
    init_balance = balance
    monthlyPayment += 10
    for x in range(12):
        init_balance -= monthlyPayment
        init_balance += init_balance * monthlyInterestRate

print("Lowest Payment: %i" % monthlyPayment)