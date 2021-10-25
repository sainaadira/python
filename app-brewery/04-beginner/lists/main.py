'''
##################################################################
      LISTS - data stucture. organizing and storing data 
      (like an array)
      keep pieces of data that have a relationship
      help maintain order

further reading: https://docs.python.org/3/tutorial/datastructures.html?highlight=data%20structures
##################################################################

'''

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
