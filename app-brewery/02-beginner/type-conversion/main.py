# TYPE CONVERSION - changing data type from one type to another
# works the same as JS but instead i'm not using the String obj to convert a number to a string, i'll be using: str() function instead

num_char = len(input('what is your name?'))
new_num_char = str(num_char)
print('your name has ' + new_num_char + ' characters.')
# prints: your name has 3 characters.

# to type check use the type() function
print(type(1234))  # prints : <class 'int'>


#___________  type conversion exercise____________ #

# 🚨 Don't change the code below 👇

two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

first_num = two_digit_number[0]
second_num = two_digit_number[1]
result = int(first_num) + int(second_num)
print(result)
