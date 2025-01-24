"""
Author: Gabi Costa
Assignment / Part: HW1 - Q4
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter your amount of dollars and cents, in two separate lines.")
dollar_value = int(input())
cent_value = int(input())

cents_in_dollar = 100

total_cents = int(cent_value + (dollar_value * cents_in_dollar))

quarter_in_cents = 25
dime_in_cents = 10
nickel_in_cents = 5
penny_in_cents = 1

number_of_quarters = int(total_cents/quarter_in_cents)
cents_left = total_cents % quarter_in_cents
number_of_dimes = int(cents_left/dime_in_cents)
cents_remaining = cents_left % dime_in_cents
number_of_nickels = int(cents_remaining/nickel_in_cents)
number_of_pennies = cents_remaining % nickel_in_cents

print(dollar_value, 'dollars and', cent_value, 'cents are:', number_of_quarters, 'quarters,', number_of_dimes, 'dimes,', number_of_nickels, 'nickels and', number_of_pennies, 'pennies')





