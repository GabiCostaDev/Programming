"""
Write a program that asks the user to input a positive integer, and
print a triangle of numbers aligned to the left, where the first line
contains the number 1 . The second line contains the numbers 2 , 1 .
The third line contains 3 , 2 , 1 . And so on. Surrounding your triangle
should be a "frame" composed of the plus '+' , minus '-' , and pipe '|'
characters.

"""

nth_term = int(input('Please enter a positive integer: '))

width = 2 * nth_term - 1

print('+' + '-' * width + '+')

next_term = 1

for x in range(1, nth_term + 1):
    line = ''
    for y in range(x, 0, -1):
        line += str(y) + ' '
    line = line.strip()
    print('|' + line.ljust(width) + '|')

print('+' + '-' * width + '+')

