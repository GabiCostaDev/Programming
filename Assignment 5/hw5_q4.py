"""
Starting from the last character of the sentence, you must read every X-th letter.
If the character that you land on is a number, you must skip it. start at the last
character, skip 2 (as denoted by the decryption key), and ignore the one numeric
character landed on. You may assume that both user inputs will always be valid ones.
You may not use the reverse() string method.

"""

original_string = input('Enter an encoded string: ')
key = int(input('Enter a key: '))

reversed_string = original_string[::-1]
new_string = ''

for i in range(0, len(reversed_string), key+1):
    if not reversed_string[i].isdigit():
        new_string += reversed_string[i]
print(new_string)
