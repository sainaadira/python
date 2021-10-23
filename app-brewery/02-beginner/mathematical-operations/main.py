# MATHEMATICAL OPERATORS #

3 + 5
8 - 1
3 * 2
3 ** 2
6 / 3  # when you divde you'll always get a float in python

# PEMDASLR
#  ()
#  **
#  * /
#  + -


print(3 * 3 + 3 / 3 - 3)  # prints: 7
# code broken down
# 3 * 3 = 9
# 3/3 = 1
# 9 + 1 = 10
# 10 - 3 = 7


#_____ BMI EXERCISE ______#

# 🚨 Don't change the code below 👇
height = input("enter your height in ft: ")
weight = input("enter your weight in lbs: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = int(weight) / int(height) ** 2
print(int(bmi))
