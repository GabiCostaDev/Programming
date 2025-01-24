"""
Write a simple version of the card banking game twenty-one (or vingt un
in a superior language) as if the banker were a random number generator
and the only two punters were you and the computer.

Your program should:
- Ask the user whether they want to play twenty-one. They may only enter
the characters 'y' for "yes" and 'n' for "no". If the player chooses "no",
then the game simply ends. Your program must continue asking the player
for input until the user enters either 'y' or 'n'.
- If the player chooses to play, your program must "give them" two random
cards of values [1, 11].
- The program must then show the player the value of these two cards.
- The program will then ask the player whether they want a third card or
not to put their score closer to 21. Again the program must continue asking
the user for input until they enter 'y' for "yes" or 'n' for "no".
	* If the user entered 'y' , generate another random card of value [1, 11].
	The user's total score in this case will be the value of all three cards
	added together.
	* If the user entered 'n' , the user's total score in this case will be
	the value of the first two cards added together.
- Generate the user's opponent's score by generating a random number in the
range of [0, 100]. Your program should re-generate another random number until
this number falls between 3 and 33. Of course we could simply generate number
between 0 and 33 instead, but this adds a bit more entropy to the process.
- Print a message letting the user know who won.
	* The user automatically wins if they score a 21 and the computer doesn't.
	* The computer automatically wins if they score a 21 and the user doesn't.
	* The user also wins if their score is closer to (but not higher than) 21
	than the computer's score.
	* The computer wins if their score is closer to (but not higher than) 21
	than the user's score.
	* There is a draw/tie if both players scored the same score and/or if both
	of their scores are above 21.

"""
import random

while True:
    choice = input("Would you like to play 'Twenty-One'? [y/n] ").lower()
    if choice in ['y', 'n']:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if choice == 'y':
    n1 = random.randint(1, 11)
    n2 = random.randint(1, 11)
    print("Your cards are worth", n1, "and", n2)
    score = n1 + n2

    while True:
        opponent_score = random.randint(0, 100)
        if 3 <= opponent_score <= 33:
            break

    print("Your score is " + str(score) + "!")
    print("Your opponent's score is " + str(opponent_score) + "!")

    if score > 21:
        if opponent_score > 21:
            print("It's a draw!")
    elif score > opponent_score:
        print("You win! Your score was " + str(score) + ".")
    else:
        print("You lose. Your opponent's score was " + str(opponent_score) + ".")

    choice = input("Would you like another card? [y/n] ").lower()
else:
    print('Thank you for playing!')
