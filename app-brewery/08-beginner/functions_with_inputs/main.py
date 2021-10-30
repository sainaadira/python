"""
#######################################################
functions with inputs

def my_function(param):
  # do something
  # do something else

my_function(arg)

#######################################################
"""
import math
import random
# a simple function
name = input('What is your name? ')


def greet():
    print(f'hello, {name}')
    print(f'bonjour, {name}')
    print(f'jambo, {name}!')


greet()


# a function that allows inputs
def greet2(name):
    print(f'hello {name}')


greet2('sai')

# choosing a random name to greet
random_name = random.choice(['mat', 'jim', 'tim', 'kim'])


def greet2(name):
    print(f'hello {name}')


greet2(random_name)


# functions with more than one input
names = random.choice(['jess', 'mat', 'zoe', 'jan'])
locations = random.choice(['chicago', 'boston', 'dc', 'philly'])


def greet_with(name, location):
    print(f'{name} is from {location}')


greet_with(names, locations)

"""
#######################################################
              ** keyword arguments **
you can add each param names to set first param = a 
so when you change the order of the agruments, the
values are still bound together.

syntax:

def my_function(a, b, c):
  # do something
  # do something else

my_function(a = 1, b = 2, c = 3)

#######################################################
"""


def greet_person(name, location):
    print(f'hey, {name}, what\'s it like in {location}?')


greet_person(name='zöe', location='chicago')


"""
#######################################################
code exercise: paint area calculator
given a height and width
calculate how many cans of paint you'll need

roudnd up to the nearest whole number

#######################################################
"""

# Write your code below this line 👇

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    num_of_cans = math.ceil(height * width / cover)

    print(f'you\'ll need {num_of_cans} to paint your wall.')


paint_calc(height=test_h, width=test_w, cover=coverage)


"""
#######################################################
code exercise: prime number checker
number that is only divisible by 1 and itself

#######################################################
"""


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('It is a prime number')
    else:
        print('It is not a prime number')


n = int(input("Check this number: "))
prime_checker(number=n)
