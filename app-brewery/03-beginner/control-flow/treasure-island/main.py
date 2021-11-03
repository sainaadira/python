''''
TREASURE ISLAND
flow chart: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#G1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi

choose your own adventure and use if, elif, else to help guide the path towards the treasure
'''


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'Two paths in the jungle lead to a lake which path will you take? Type: left or right \n').lower()
if choice1 == 'left':
    choice2 = input('You arrive at the lake and there\'s a boat that will take you to the house where the treasure is. However, there\'s a stom coming. Do you swim or wait? Type: swim or wait \n').lower()
    if choice2 == 'wait':
        choice3 = input(
            'You arrive at the house where the treasure lies behind one of 4 doors. Type: red, blue, yellow or purple ').lower()
        if choice3 == 'yellow':
            print('You win!')
        elif choice3 == 'red':
            print('You are burned by fire. Game over!')
        elif choice3 == 'blue':
            print('You are eaten by beasts. Game over!')
        elif choice3 == 'purple':
            print('Game over')
    else:
        print('You are attacked by a trout. Game over!')
else:
    print('You fall into a hole. Game over!')
