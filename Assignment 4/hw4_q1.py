"""
Print the powers of a user-input number up until a
certain limit (which the user will also determine). Write
a problem that will do this, but will only print the even
(i.e. 2, 4, 6, etc.) powers, and will do so backwards. You
may not assume that the user will enter whole-number values;
they can also enter floating-point values. Your program
should keep asking the user to enter both of these values
until they are positive, non-zero, whole-number values.

"""


base = int(input('Please enter a positive integer to serve as the base: '))

while base <= 0:
    print('Invalid value for the base (' + str(base) + ').')
    base = int(input('Please enter a positive integer to serve as the base: '))

highest_power = int(input('Please enter a positive integer to serve as the highest power: '))

while highest_power < 0:
    print('Invalid value for the highest power (' + str(highest_power) + ').')
    highest_power = int(input('Please enter a positive integer to serve as the highest power: '))

if highest_power % 2 != 0:
    highest_power -= 1

for num in range(highest_power, -1, -2):
    print(f'{base} ^ {num} = {base ** num}')
