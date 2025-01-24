"""
Write a program that asks the user to input a string containing only lower case letters (you may assume that they
will do so). Your program should determine if the input is ordered in lexicographic decreasing order. If it is not
in decreasing order, then your program must also print the location at which the string stops being ordered in
decreasing order.

"""

string = input('Please enter a string: ')
is_decreasing = True
location = 0
while location < len(string) - 1 and is_decreasing:
    if string[location] < string[location+1]:
        is_decreasing = False
    location += 1

if is_decreasing:
    print(string, 'is decreasing')
else:
    print(string, 'is not decreasing')
    print('It stopped being lexicographically decreasing at location', location)
