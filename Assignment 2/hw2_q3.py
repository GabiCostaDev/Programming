"""
Write a program that reads a number of days, hours, and
minutes that each of them worked, and prints the total
time both of them worked together in the same format.

"""

days_semi = int(input('Please enter the number of days Semi has worked: '))
hours_semi = int(input('Please enter the number of hours Semi has worked: '))
min_semi = int(input('Please enter the number of minutes Semi has worked: '))
days_daniel = int(input('Please enter the number of days Daniel has worked: '))
hours_daniel = int(input('Please enter the number of hours Daniel has worked: '))
min_daniel = int(input('Please enter the number of minutes Daniel has worked: '))

days = days_semi + days_daniel
hours = hours_semi + hours_daniel
min = min_semi + min_daniel

# Convert extra minutes into hours
extra_hours = min // 60
min = min % 60
hours += extra_hours

# Convert extra hours into days
extra_days = hours // 24
hours = hours % 24
days += extra_days

print('The total time both of them worked together is: ', days, 'days, ', hours, 'hours and', min, 'minutes')