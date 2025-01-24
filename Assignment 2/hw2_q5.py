"""
Let's say that we are developing a video-game where the user's
level is determined by their current experience points (XP).
For this problem, the user will enter their current XP as input
and the program will output their current level.

"""

current_xp = float(input("Enter this user's current XP: "))
current_xp = round(current_xp, 1)

if current_xp < 0:
    print('ERROR: Experience points cannot be negative.')
elif current_xp < 15.0:
    print('Level 1 Player (XP: ' + str(current_xp) + ')')
elif 15.0 <= current_xp < 25.0:
    print('Level 2 Player (XP: ' + str(current_xp) + ')')
elif 25.0 <= current_xp < 30.0:
    print('Level 3 Player (XP: ' + str(current_xp) + ')')
elif 30.0 <= current_xp < 40.0:
    print('Level 4 Player (XP: ' + str(current_xp) + ')')
elif 40.0 <= current_xp < 60.1:
    print('Level 5 Player (XP: ' + str(current_xp) + ')')
else:
    print('ERROR: Please enter a valid XP value.')
