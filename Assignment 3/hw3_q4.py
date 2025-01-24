"""
Ask the user to input a positive integer, say, n , and print all
the numbers from 1 to n that have more even digits than odd digits.
For example, the number 134 has two odd digits ( 1 and 3 ) and one
even digit ( 4 ), therefore it should not be printed. Printing
should occur all on one line, separated by spaces.

"""

nth_term = int(input('Please enter a positive integer: '))

for i in range(1, nth_term + 1):
    even = 0
    odd = 0
    check = i
    while check > 0:
        if check % 2 == 1:
            odd += 1
        else:
            even += 1
        check = check // 10
    if even > odd:
        print(i, end=' ')

