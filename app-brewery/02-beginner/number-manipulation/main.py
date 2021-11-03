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
