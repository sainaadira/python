# printng first code
print('hello world')

# variables
# if you want to create variables with more than 1 word, use underscore
age = 20
age = 30
first_name = 'sai'
is_Online = False
print(age)


# exercise
name = 'john smith'
age = '20'
is_new_patient = True

# receiving input from user
input('what is your name? ')


# data types
birth_year = input('enter your birth year: ')
your_age = 2021 - int(birth_year)
print(your_age)

# built-in functions for converting #️'s

# int() - converts string to integer
# float() converts number to decimal
# bool() - converts number to a boolean
# str() - converting a value into a string


# exercise - create a calculator that sums two numbers
first_num = input('num 1: ')
second_num = input('num 2:')
sum = int(first_num) + int(second_num)
print('sum is: ' + str(sum))


# __________strings and methods___________

course = 'python for beginners'
course.upper()  # converts string to uppercase
course.lower()  # converts string to lowercase
course.find('y')  # returns the index of first occurence of y in course string
# in is a special keyword and it chrcks to see if python is in course, returns boolean
course.find('python' in course)
course.replace('for', '4')  # replace 'for' with '4' => 'python 4 beginners'


# mathematic operators
#   +
#   -
#   /
#   *
#   //
#   **

# augmentic operators
#  +=
#  -=
#  /=
#  *=


# ____________comparison operators - returns a boolean________

#  <  - greater than

#  <=  greater than or equal to

#  >  less than

#  >=  less than or equal to

#  ==  equal to

#  != not equal to


# ____________logical operators______________

# and
price = 26
print(price > 10 and price < 30)  # prints True

# or
price_2 = 5
print(price_2 > 10 or price_2 < 30)  # prints True

# not - inverses any values that you give it
price_3 = 5
print(not price_3 > 30)  # prints true


# _____________if statements: control flow________________

#  NO CURLY BRACES or parenthesis
#  indentation represents a block of code
# separate conditions with a colon
# within the if block, the code indented represents the then- statement
# elf - is short for else if

temperature = 25
if temperature > 30:
    print('it\'s a hot day')
    print('drink plenty of water')
elif temperature > 20:
    print('it\'s a nice day')
elif temperature > 10:
    print('it\'s a bit cold')
else:
    print('time to hibernate')

# _____________exercise: ________________
# get users weight and convert to kg or lbs based on user input

user_weight = float(input('weight: '))
conversion_option = input('(K)g or (L)bs: ')


if conversion_option() == 'K':
    converted = user_weight / 0.4
    print('your weight in kg is: ' + str(converted))
else:
    converted = user_weight * 0.45
    print('weight in lbs is: ' + str(converted))


# _____________while loops________________

i = 1
while i <= 5:
    print(i * '*')
    i += 1

    # prints:
    #  *
    #  **
    #  ***
    #  ****
    #  *****


# _____________lists: similar to arrays in js____________

names = ['john', 'bob', 'mosh', 'sam', 'larry']
print(names[3])  # prints: mosh

# grabs first elements from start to end index ['john', 'bob', 'mosh']
print(names[0:3])


# _____________lists: methods_____________
numbers = [1, 2, 3, 4, 5]

# adding numbers to end of list
numbers.append(6)   # prints: [1 ,2, 3, 4, 5, 6]

# adding numbers to beinning or middle
# syntax insert(index: int, obj: any data type)
numbers.insert(0, -1)  # prints [-1, 1, 2, 3, 4, 5]

# removing items from a list
numbers.remove(3)   # prints [1,2,4,5]

# removing all of the items in the list - does not expect any values
numbers.clear()   # prints: []


# checking to see if values exist in list
print(1 in numbers)   # prints: True
print(10 in numbers)   # prints: False

# to check how many values are in the list
print(len(numbers))  # prints: 5


# _____________for loops: iterating through items in list____________

for items in numbers:
    print(item)

# now doing this with a while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

    # _____________range: generates sequence of numbers____________
    # range(starting val: 5, ending val: 10, step: 2) - ending value is excluded from sequence
    # the third param lets you skip over numbers in sequence by specified number

for number in range(5):
    print(number)
    # prints 0,1,2,3,4


# _____________tuples: sort of like lists, used to store sequence of objects____________
# they're immutable and cannot be changed once created
# lists have [ ]  & tuples have ( )

nums = (1, 2, 3)
# count -  returns number of occurences of an element elements
# index- returns first occurence of a given elemebt
