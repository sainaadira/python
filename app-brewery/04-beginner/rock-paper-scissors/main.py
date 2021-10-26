import random

user_choice = int(input('your choices -  0: rock, 1: paper, 2: scissors '))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# storing images in a list
game_img = [rock, paper, scissors]
# grab the image and the user choice is the index
print(f'you chose: {game_img[user_choice]} \n')

# choosing a random int between 0,2 for computer
random_cpu_choice = random.randint(0, 1)
print(f'computer chose: {game_img[random_cpu_choice]} \n')

# check to see if user types number between 0-2
if user_choice >= 3 or user_choice < 0:
    print('you typed an invalid number, you lose!')
    # if user choses rock and cpu choses scisors: user wins
if user_choice == 0 and random_cpu_choice == 2:
    print('you win')
    # if computer chooses rock and user choses scisors: user loses
elif random_cpu_choice == 0 and user_choice == 2:
    print('you lose')
    # if computer choice is greater than user choice: user loses
elif random_cpu_choice > user_choice:
    print('you lose')
    # if user choice is greater than computer choice: user wins
elif user_choice > random_cpu_choice:
    print('you win!')
    # if both are same choices: it's a tie
elif user_choice == random_cpu_choice:
    print('it\'s a tie, try again')
