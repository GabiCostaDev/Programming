"""
Write a program that will ask the user to enter the value of HPmax.
From there, your program must generate the following pseudo-random values:
 - The Pokémon's current health, which can be any value between and including 1 and HPmax.
 - The PokéBall's Ball value which, again, is a value between and including 0 and 255.

"""
import random

max_health = int(input('Enter the max health of this Pokémon: '))
current_health = random.randint(1, (max_health+1))
ball = random.randint(1, 255)

f = math.floor((max_health*255*4)/(current_health*ball))

if f >= ball:
    print("You've caught the Pokémon")
else:
    print("Oh no! The Pokémon broke free!")