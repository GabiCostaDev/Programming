"""
Write a program that computes the cost of a long-distance call.
The cost of the call is determined according to the following rate schedule:
- Any call started between 530 A.M. and 900 P.M. (inclusive on both ends), Monday through Thursday, is billed at a rate of $0.55 per minute.
- Any call starting before 530 A.M. or after 900 P.M., Monday through Thursday, is charged at a rate of $0.35 per minute.
- Any call started on a Friday, Saturday, or Sunday is charged at a rate of $0.10 per minute.

The input will consist of:
- The day of the week
- The time the call started
- The length of the call in minutes

The output will be the cost of the call.
A few things to keep in mind:
The time must be input as a 4-digit number, representing the time in military,
or 24-hour, time. For example, the time 1:30 P.M. corresponds to the input 1330

The day of the week must be read as one of the following three character strings:
- "Mon"
- "Tue"
- "Wed"
- "Thr"
- "Fri"
- "Sat"
- "Sun"

The number of minutes will be input as a positive integer.
You can assume the user will always enter valid inputs.

"""

day = input('Enter the day the call started at: ')
time = int(input('Enter the time the call started at (hhmm): '))
duration = int(input('Enter the duration of the call (in minutes): '))

if (time >= 530) and (time <= 2100) and (day == 'Mon' or day == 'Tue' or day == 'Wed' or day == 'Thr'):
    total_cost = 0.55 * duration
    print('This call will cost $' + str(round(total_cost, 1)))
elif ((time < 530) or (time > 2100)) and (day == 'Mon' or day == 'Tue' or day == 'Wed' or day == 'Thr'):
    total_cost = 0.35 * duration
    print('This call will cost $' + str(round(total_cost, 1)))
elif day == 'Fri' or day == 'Sat' or day == 'Sun':
    total_cost = 0.10 * duration
    print('This call will cost $' + str(round(total_cost, 1)))
else:
    print('ERROR: Please enter a valid day.')
