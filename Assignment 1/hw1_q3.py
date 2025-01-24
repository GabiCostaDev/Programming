"""
Author: Gabi Costa
Assignment / Part: HW1 - Q3
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter number of coins:")
number_of_quarters = int(input("Number of quarters: "))
number_of_dimes = int(input("Number of dimes: "))
number_of_nickels = int(input("Number of nickels: "))
number_of_pennies = int(input("Number of pennies: "))

quarter_in_cents = 25
dime_in_cents = 10
nickel_in_cents = 5
penny_in_cents = 1

total_cents = int((number_of_quarters * quarter_in_cents) + (number_of_dimes * dime_in_cents) + (number_of_nickels * nickel_in_cents) + number_of_pennies)

cents_in_dollar = 100

dollar_value = int(total_cents/cents_in_dollar)

cent_value = total_cents - (dollar_value * cents_in_dollar)

print('The total is', dollar_value, 'dollar(s) and', cent_value, 'cent(s)')