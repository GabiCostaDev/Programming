"""
Write a program that:
 - Asks the user how many players will be playing in this round of Monopoly. This value must be a positive,
 non-zero integer, but you can assume that the user will never enter a float value.
 - Once they do so, each player will enter the values of each of their properties/assets. You can assume that
 these will always be positive numerical values or the characters
"DONE"
 when they are finished.
 - Once a player enters all the values, the game will print out the sum of the assets' values.
 - The program repeats steps 2 and 3 until all players have been accounted for.
 - At the very end, the program will print a congratulatory message to the winner. You don't have to worry
 about two players getting the same score

"""

number_of_players = int(input('How many players played this round? '))
while number_of_players < 0:
    number_of_players = int(input('Invalid input. How many players played this round? '))

player_number = 1
winner_total = 0
winner = 0

for num in range(1, number_of_players + 1):
    done = False
    total = 0
    while not done:
        value = input('Enter the value of a property/asset, or DONE to finish: ')
        if value == 'DONE':
            done = True
        else:
            total += float(value)

    print('Player', player_number, 'has', total, 'dollars.')

    if total > winner_total:
        winner_total = total
        winner = player_number

    player_number += 1

print('Congratulations, player ' + str(winner) + '! You won with $' + str(winner_total) + '!')
