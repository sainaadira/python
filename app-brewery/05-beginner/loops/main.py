'''
###############################################################
FOR LOOPS-
iterating through each item inside of a list

for [item] in [list_of_items]:
  # do something here

###############################################################
'''
fruits = ['apple', 'kiwi', 'banana', 'mango']
for fruit in fruits:
    print(fruit + ' pie')

# prints:
# apple pie
# kiwi pie
# banana pie
# mango pie


'''
###############################################################
code challenge:
get the average of student heights
based on the given input 
round average to the nearest whole number

###############################################################
'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# intialize height sum at 0
height_sum = 0

# loop through each student in list and add height to sum
for heights in student_heights:
    height_sum += heights
print(height_sum)

# initalize student count at 0
no_of_students = 0

# loop through each student and increment by 1
for student in student_heights:
    no_of_students += 1
print(no_of_students)

# get average height: divide height by number of students
# round total to nearest whole number
average_height = round(height_sum / no_of_students)
print(average_height)


'''
###############################################################
code challenge:
get the highest score in the class 
set max_score and intalize to 0
loop through student_scores
check if score is greater than max_score
if so: max score is now set to highest score from student_scores

###############################################################
'''


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

max_score = 0
for scores in student_scores:
    if scores > max_score:
        max_score = scores
print(f'the highest score in the class is: {max_score}')


'''
###############################################################
for loop with range
range(a,b) goes through every number between a & b(not inclusive)
range (a,b, 2) - skipping every 2 numbers in the range

###############################################################
'''

total = 0
for number in range(1, 101):
    # adds every number in range to the total starting from 0
    # sums every number from 1 -100
    total += number
print(total)  # prints: 5050


'''
###############################################################
for loop with range
range(a,b) goes through every number between a & b(not inclusive)
range (a,b, 2) - skipping every 2 numbers in the range

adding even numbers
###############################################################
'''

even_total = 0
for num in range(1, 101, 2):
    even_total += num
print(even_total)  # prints: 2500


'''
###############################################################
fizzbuzz in python
###############################################################
'''

# Write your code below this row 👇

for number in range(1, 101):
    # print(number)
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
