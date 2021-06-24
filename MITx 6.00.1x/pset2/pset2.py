balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def remaining_balance(months, balance, monthlyPaymentRate, annualInterestRate):
    for i in range(months):
        unpaid_balance = balance - balance * monthlyPaymentRate
        balance = unpaid_balance + annualInterestRate / 12.0 * unpaid_balance
    return balance

result = remaining_balance(12, balance, monthlyPaymentRate, annualInterestRate)
print("Remaining balance: " + str(round(result, 2)))


balance = 3329
annualInterestRate = 0.2


def min_fixed_monthly_payment(months, balance, annualInterestRate):
    payment = 10
    while True:
        unpaid = balance
        for i in range(months):
            monthlyInterestRate = annualInterestRate / 12.0
            monthlyUnpaidBalance = unpaid - payment
            unpaid = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        if unpaid <= 0:
            break
        payment += 10
    return payment

result = min_fixed_monthly_payment(12, balance, annualInterestRate)
print("Lowest Payment: " + str(round(result, 2)))


balance = 999999
annualInterestRate = 0.18

def bisection_search(months, balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lower = balance / months
    upper = balance * (1 + monthlyInterestRate) ** months / months
    payment = (lower + upper) / 2
    while True:
        unpaid = balance
        for i in range(months):
            monthlyUnpaidBalance = unpaid - payment
            unpaid = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        if .01 >= abs(unpaid) >= -.01:
            break
        elif unpaid > .01:
            lower = payment
        else:
            upper = payment
        payment = (lower + upper) / 2
    return payment



result = bisection_search(12, balance, annualInterestRate)
print("Lowest Payment: " + str(round(result, 2)))
