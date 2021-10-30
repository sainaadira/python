"""
#####################################################################
 dictionaries (hash map in js)
    {
     'key': value,
     'key': value
     }
#####################################################################
"""
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.',
}

# retrieving something from a dictionary
print(programming_dictionary['Bug'])
# prints: An error in a program that prevents the program from running as expected.


# adding data into a dictionary
programming_dictionary['Loop'] = 'Code that does a task repeatedly'
print(programming_dictionary)

# wipe out an existing dictionary
programming_dictionary = {}


# editing values based on on key
programming_dictionary['Bug'] = 'A moth in your computer'

# prints: {
#  'Bug': 'A moth in your computer',
#  'Function': 'A piece of code that you can easily call over and over again.',
# 'Loop': 'Code that does a task repeatedly'
# }

# looping through keys in dictionary
for key in programming_dictionary:
    print(key)
    # to get the values
    print(programming_dictionary[key])


"""
#####################################################################
code challenge:
You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
#####################################################################
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


# 1: Create an empty dictionary called student_grades.
student_grades = {}

# 2: Write your code below to add the grades to student_grades.👇
# loop through the dictionary
# for each student, calculate score
# condtionally add grades based on score
# add values to the student_grades dictionary

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)


"""
#####################################################################
                            nesting

                    {
                        key: [list],
                        key: {dict}
                    }
#####################################################################
"""

# nesting
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# nesting a list in a dictionary
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin' 'Hamburg', 'Stuttgart'],
}

# nesting dictionary in a dictionary
travel_log = {
    'France': {'cities_visited': ['Paris' 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin' 'Hamburg', 'Stuttgart'], 'total_visits': 5},
}

# nesting dictionaries in lists
travel_log = [
    {
        'country': 'France',
        'cities_visited': ['Paris' 'Lille', 'Dijon'],
        'total_visits': 12,
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin' 'Hamburg', 'Stuttgart'],
        'total_visits': 5,
    },
]


"""
#####################################################################
 coding exercise:
 You are going to write a program that adds to a travel_log. 
 You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code
to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.
#####################################################################
"""
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country_visited, num_of_visits, cities):
    new_country = {}
#  give new dictionary the same pieces of data
    new_country['country'] = country_visited
    new_country['visits'] = num_of_visits
    new_country['cities'] = cities
#  adding new_country dictionary to travel_log list
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
