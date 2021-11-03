'''
##################################################################
    TIP CALCULATOR PROJECT


# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
##################################################################

'''

# all inputs to gather info for calculation
print('Welcome to the tip calculator \n')
bill = float(input('What is the total bill? $ '))
tip = int(input('What percent would you like to give? Type: 10, 12, 15: '))
people_paying = int(input('How many people will split the bill? '))


# grab percentage
tip_as_percent = tip / 100

# add percentage to bill
bill_with_tip = bill * tip_as_percent

# get total bill amount with tip
total_amount = bill + bill_with_tip

# divide total amount by people people_paying
# round up number and stop 2 places after decimap
final_amount = round(total_amount / people_paying, 2)

# display final amount
print(f'Each person will pay ${final_amount}')
