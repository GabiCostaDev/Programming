"""
Our goal is the following:
- Ask the user to enter any notes into the arpeggiator. The arpeggiator will check whether
these notes are actual valid musical notes, so you don't need to worry about checking yourself.
When the user is done entering notes, they should enter the word "DONE" (caps-sensitive). The
user must do this to proceed.
- Next, the user will enter a direction in which they would like the arpeggiator to play. Their
choices are limited to the characters 'U' for "up" and 'D' for "down". The user must enter either
of these characters to proceed.
- Next, the user must enter how many times they would like their arpeggiator to play. The user
must enter a positive, non-zero number to proceed.
- Finally, the program should play the arpeggiator as many times and in the direction that the
user selected.

"""
import arpeggiator

ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

note = ''
while note != 'DONE':
    note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")
    if note != 'DONE':
        ARPEGGIATOR.add_note(note)

print()
direction = ''
while direction != 'U' and direction != 'D':
    direction = input("Enter an arpeggiator direction [U/D] ")

if direction == 'U':
    direction = UP
else:
    direction = DOWN
print()
repeat = int(input('How many times do you want your arpeggiator to play? '))
while repeat <= 0:
    repeat = int(input('How many times do you want your arpeggiator to play? (Must be a positive amount) '))
print()
for i in range(repeat):
    ARPEGGIATOR.play(direction)

