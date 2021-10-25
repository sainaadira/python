# ____________ conditional statements____________

""""
# syntax

if condition:
  do this
else:
   do this

"""

# example used: bathtub, if water level reaches certain level, water gets drained
# otherwise, the tub will continue to fill

water_level = 50
if water_level > 80:
    print('drain the water')
else:
    print('continue filling tub')

""""
real life example 1: you're at a park and in order to purchase tickets for a ride, they must be > 120cm
 -- so i need to check what their height is
 -- if their height is > 120cm, they can ride
 -- if their height is < 120cm, they cannot ride
"""

""""
nested else/if statement
the first condition needs to be true in order for the 2nd condition to run

if condition:
  do this
  if another condition:
     do this
  else:
    do this
else:
  do this


real life example 1a:  in addition to checking their height, now you need to check their age

if age <= 18  tickets: $7
if age > 18   tickets: $12

if age  < 12    ticket: $5
if age 12 - 18  ticket: $7
if age > 18     ticket: 12

want photos
yes : add 3 dollars to their ticket price
no: return their bill without extra charge


"""


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print('you can purchase your ticket')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('children tickets are $5 dollars')
    elif age <= 18:
        bill = 7
        print('youth tickets are $7 dollars')
    elif age >= 45 and age <= 55:
        print('do not worry, you can ride for free')
    else:
        bill = 12
        print('adult tickets are $12 dollars')

    wants_photo = input('do you want photos? Y or N')
    if wants_photo == 'Y'.upper():
        bill += 3

    print(f'your total bill is {bill}')

else:
    print('sorry, you\'ll get to ride soon though!')


""""
code exercise: use conditional to check if a number is odd or even
"""

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

    """"
code challenge:
based on the user input, calculate the bmi

bmi formula: weight / height ^ 2
based on the condtions, write a program that prints the following 

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f'your bmi is {bmi}: you are underweight')
elif bmi < 25:
    print(f'your bmi is {bmi}: you have a normal weight')
elif bmi < 30:
    print(f'your bmi is {bmi}: you are slightly overweight')
elif bmi < 35:
    print(f'your bmi is {bmi}: you are obese')
else:
    print(f'your bmi is {bmi}:you are clinically obese')


""""
code challenge:

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

on every year that is evenly divisible by 4
 **except** every year that is evenly divisible by 100 
 **unless** the year is also evenly divisible by 400

"""

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print('not leap year')


""""
code challenge:
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
total_bill = 0
# Write your code below this line 👇

# checking the size of each pizza and adding price to each
if size == 'S':
    total_bill += 15
elif size == 'M':
    total_bill += 20
else:
    total_bill += 25

# add $2 or $3 depending on size
if add_pepperoni == 'Y':
    if size == 'S':
        total_bill += 2
    else:
        total_bill += 3

# add $1 to all sizes
if extra_cheese == 'Y':
    total_bill += 1

print(f'your total bill is: {total_bill}')


# logical operators
# and - both condtions have to be true
# or - either one or the other condtion needs to be true
# not - reverses a condtion, if true then it becomes false, if false then it becomes true


""""
code challenge:
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."


"""


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# combine both couples' names
couples = name1 + name2
# convert to lowercase letters
couples = couples.lower()

# checking to see if the occurences of true/love appear
# count is a function that counts no. of occurrences in a string
t = couples.count('t')
r = couples.count('r')
u = couples.count('u')
e = couples.count('e')
true = t + r + u + e

l = couples.count('l')
o = couples.count('o')
v = couples.count('v')
e = couples.count('e')
love = l + o + v + e

# turning true/love into a string for concatenation
# converting it into an integer for comparison
love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(
        f'your love score is {love_score}, you go together like coke and mentos')
elif love_score >= 40 and love_score <= 50:
    print(f'your love score is {love_score}, you are alright together')
else:
    print(f'your love score is {love_score}')
