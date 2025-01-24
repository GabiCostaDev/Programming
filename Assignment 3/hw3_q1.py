"""
Write a program that asks the user to input three floating-point numbers:
a , b , and c (just this once, only these three single-letter variables
will be permitted). These are the parameters of the quadratic equation.


Classify the equation as one of the following:

Infinite number of solutions
    --> For example: a = 0 , b = 0 , c = 0
No solution
    --> For example: a = 0 , b = 0 , c = 4
No real solution
    -->  For example: a = 1 , b = 0 , c = 4
One real solution
    --> In cases there is one real solution, please print the solution.
Two real solutions
    --> In cases there are two real solutions, please print the solutions.

"""
import math

a = float(input('Please enter value of a: '))
b = float(input('Please enter value of b: '))
c = float(input('Please enter value of c: '))

discriminant = b**2 - 4*a*c

if a == 0 and b == 0:
    if c == 0:
        print('This equation has an infinite number of solutions.')
    else:
        print('This equation has no solutions.')
else:
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print('This equation has 2 solutions: x = ', x1, 'x = ', x2)
    elif discriminant == 0:
        x1 = -b / (2 * a)
        print('This equation has 1 solution: x = ', x1)
    else:
        print('This equation has no real solution.')



