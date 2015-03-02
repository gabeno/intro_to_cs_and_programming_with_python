'''
Now write a program that calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months. By a fixed monthly payment,
we mean a single number which does not change each month, but instead is a constant
amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay
off all debt in under 1 year, for example:

    Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the
end of the month (after the payment for that month is made). The monthly payment
must be a multiple of $10 and is the same for all months. Notice that it is
possible for the balance to become negative using this payment scheme, which is
okay. A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 3926 # 4773 # 3329
annualInterestRate = 0.2

monthly_payment = 0
monthly_rate = annualInterestRate / 12.0
remaining_balance = balance
while (remaining_balance > 0):
    new_balance = balance
    monthly_payment += 10
    # print 'Monthly payment: %s' % monthly_payment
    # print 'starting balance: %s' % new_balance

    for month in range(1, 13):
        unpaid_balance = new_balance - monthly_payment
        interest_paid = monthly_rate * unpaid_balance
        new_balance = unpaid_balance + interest_paid
        # print 'remaining balance: %s' % new_balance
    remaining_balance = new_balance

# print 'remaining balance: %s' % new_balance
print 'Lowest Payment: %s' % monthly_payment
