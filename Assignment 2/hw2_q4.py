"""
Write a program that will ask the user for the Pokemon's
level and speed stat (both integer values), and print out
the move's damage multiplier. You'll want think about what
would happen if the Pokemon doesn't land a critical hit as
well. You may assume that the Pokemon's level and speed stat
will always be positive integers.

"""
import random

level = int(input("What is the Pokémon's level? "))
speed = int(input("What is the Pokémon's speed? "))

R = random.randint(0, 256)
T = speed/2

if T > R:
    threshold = speed/2
    damage_multiplier = float(((2*level) + 6)/(level + 6))
    print("The Pokémon's move will be " + str(round(damage_multiplier, 2)) + 'x stronger!')
else:
    print("The Pokémon's move will be 1x stronger!")


