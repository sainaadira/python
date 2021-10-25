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
    'you\'re walking down a path that separates: go left or right \n').lower()
if choice1 == 'left':
    choice2 = input(
        'the tide is will rise sometime in the afternoon but the treasure is at the house across the lake: swim or wait? \n').lower()
    if choice2 == 'wait':
        choice3 = input(
            'you made it to the house and the treasure is behind a one of 4 doors: blue, yellow, purple or red. which one holds your fate? \n ').lower()
        if choice3 == 'red':
            print('you were burned by fire, game over')
        elif choice3 == 'yellow':
            print('you win the treasure!')
        elif choice3 == 'blue':
            print('you were eaten by beasts. game over')
        else:
            print('invalid color choice')
    else:
        print('you were eaten by an angry trout: game over')
else:
    print('you fell into a hole, game over')
