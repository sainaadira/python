# generating a random number
import random

# randint(a,b) generates random number between a b (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

# generating a random floating point # between 0-1(not inclusive)
# to expand range, muliply by a number
random_float = random.random() * 5
print(random_float)


'''
code challenge: coin flip

generate a random number between 0,1
1 - heads
2 - tails

if coin flip = 1 print 'Heads', otherwise print 'Tails' 
'''

# Write your code below this line 👇
coin_flip = random.randint(0, 1)
if coin_flip == 1:
    print('Heads')
else:
    print('Tails')
