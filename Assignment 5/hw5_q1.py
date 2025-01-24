"""
Write a program that prompts the user for a string and prints the
string in lowercase without using the lower() , upper() , islower()
and isupper() string methods. Your program must also tell the user
how many letter were made lowercase, how many letters were left
untouched, how many whitespace characters there were (i.e. ' ' and
' \n '), and how many non-alphabetic characters the string contained.
You must do this without using isalnum() , isdigit() , isalpha() ,
or any other method that checks for the type of character you are
considering. In other words, all of these checks must be made manually.

"""

something = input('Say something: ')
final = ''

changed_count = 0
unchanged_count = 0
whitespace_count = 0
nonalpha_count = 0

for c in something:
    if 'A' <= c <= 'Z':
        final += chr(ord(c) + 32)
    elif 'a' <= c <= 'z':
        final += c
    else:
        nonalpha_count += 1
        final += c
print(final)

for i in range(len(something)):
    if something[i] == ' ':
        whitespace_count += 1
    elif something[i] != final[i]:
        changed_count += 1
    elif 'a' <= something[i] <= 'z':
        unchanged_count += 1
    else:
        nonalpha_count += 1

print('Number of changed letters: ', changed_count)
print('Number of unchanged letters: ', unchanged_count)
print('Number of whitespace characters: ', whitespace_count)
print('Number of non-alphabetic characters: ', nonalpha_count)






