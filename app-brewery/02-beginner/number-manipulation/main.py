#  NUMBER MANIPULATION
# you can round numbers with the round() function
# inside the function you can specify the number decimal places you want to round the number to


print(round(8/3, 2))  # prints 2.67

# F strings # similar to string interpolation or template string in JS
score = 0
height = 5.1
isWinning = True

print(f'your score is {score}')


# _____ Age in weeks, months, years exercise ______#

# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_remaining = 90 - age
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

print(f'you have {days} days, {weeks} weeks, and {months} months left')

# You have 12410 days, 1768 weeks, and 408 months left.


# __________ TIP CALCULATOR PROJECT _________ #

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
