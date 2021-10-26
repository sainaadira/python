'''
##################################################################
      LISTS - data stucture. organizing and storing data 
      (like an array)
      keep pieces of data that have a relationship
      help maintain order

further reading: https://docs.python.org/3/tutorial/datastructures.html?highlight=data%20structures
##################################################################

'''

import random
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# change item in list
states_of_america[0] = 'Rhode Island'

# add item to end of list
states_of_america.append('Some state')

# remove specified item in list
states_of_america.remove('Some state')

# adding a bunch of items to a list
states_of_america.extend(['one', 'two', 'three'])
print(states_of_america)


"""
#############################################
code challenge: 
give everyone's name separated by a comma
randomly select a name from the list
and that person will pay the bill for everyone
################################################
"""


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


len_of_names = len(names)
randomize = random.randint(0, len_of_names - 1)
print(f'{names[randomize]} will pay buy the meal today')


"""
#############################################
working with nested lists
################################################
"""

fruits = ['Strawberries', 'Nectarines', 'Apples',
          'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes']
vegetables = ['Spinach', 'Kale', 'Celery',  'Potatoes']

# combining both lists into separate lists inside of a list: [ [fruits], [veggies] ]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

"""
prints:
[['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes'], ['Spinach', 'Kale', 'Celery', 'Potatoes']]
"""

"""
#############################################
code challenge:

################################################
"""
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = 'X'

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
