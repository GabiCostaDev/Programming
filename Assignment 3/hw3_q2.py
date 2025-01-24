"""
Write a program that reads a positive integer (say, n), and prints
the first n odd numbers (don't use n as a variable name). Write two
versions in the file, one using a for-loop, and one using a while-loop.

"""

nth_term = int(input('Please enter a positive integer: '))

n1 = 1
term = 0

print('Executing while-loop...')
while term < nth_term:
    print(n1)
    term += 1
    n1 += 2

n1 = 1

print('\nExecuting for-loop...')
for num in range(nth_term):
    print(n1)
    n1 += 2