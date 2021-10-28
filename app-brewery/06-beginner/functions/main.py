'''
###############################################################
# functions
creating a function
using the def keyword (def-ining a functing)

syntax:

def my_function():
  # do something
  # then do this
  # funally do this

my_function()
###############################################################
'''


def my_function():
    print('hello')
    print('bye')


my_function()


'''
###############################################################
hurdle challenge:
goal: get robot to jump over hurdles using commands

source: 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
###############################################################
'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_up_to_top():
    move()
    turn_left()
    move()
    turn_right()
    move()


def turn_right_move():
    turn_right()
    move()


def up_hurdle_turn_right_and_left():
    move_up_to_top()
    turn_right_move()
    turn_left()


for hurdle in range(5):
    up_hurdle_turn_right_and_left()

move_up_to_top()
turn_right_move()


#  using a while loop:

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# another while loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


'''
###############################################################
                        indendation

syntax:
    def my_function():
   •••• code here 


if/elif

  def my_function():
  •••• if sky == 'clear:'
  ••••••••print('blue')
  •••• elif sky == 'cloudy'
  •••••••• print('grey')
  •••••print('hello)
  print('world')
       
        
###############################################################
'''


'''
###############################################################
  ## while loops:
  loop that continues going while a condition is true
  once it is false, the loop will stop

  syntax:

  while something_ is_true:
    # do something here

###############################################################
'''
