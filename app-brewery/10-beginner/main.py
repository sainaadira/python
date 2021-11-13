"""
####################################################################################
                            # FUNCTIONS WITH OUTPUTS


                            def my_function():
                              result = 3 * 2
                              return result
####################################################################################
"""
# example using the return keyword


def my_function():
    return 3 * 2


my_function()


#
def format_name(fname, lname):
    first = fname.title()
    last = lname.title()

    return f'The name is {last}, {first} {last}.'


# stored into a variable to be printed
formatted_name = format_name('james', 'bond')
print(formatted_name)


# functions with multiple return statements
def format_name(fname, lname):
    if fname == '' or lname == '':
        return 'Please provide your name'
    first = fname.title()
    last = lname.title()
    return f'The name is {last}, {first} {last}.'


# stored into a variable to be printed
formatted_name = format_name('james', 'bond')
print(format_name(input('What is your first name? '),
      input('What is your last name? ')))
