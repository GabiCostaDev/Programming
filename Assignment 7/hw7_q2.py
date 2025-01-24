"""
Write a function get_root_of_average() that will accept a string parameter
representing a txt file containing a series of numbers. Your function will
also accept an integer parameter, root . What it will then do is calculate
and return the rootroot of the average of all the numbers in the file.

"""


def get_root_of_average(filename, root):

    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    total = 0
    count = 0
    current_number = ''
    for char in file.read():
        if char == ' ':
            if current_number:
                try:
                    total += float(current_number)
                    count += 1
                except ValueError:
                    print(f"WARNING: Could not cast '{current_number}' into a float.")
            current_number = ''
        else:
            current_number += char
    if current_number:
        try:
            total += float(current_number)
            count += 1
        except ValueError:
            print(f"WARNING: Could not cast '{current_number}' into a float.")
    file.close()
    if root == '':
        root = 2
    if count == 0:
        return 0
    else:
        average = total / count
        cube_root = average ** (1/root)
        return cube_root


def main():

    cubed_root = get_root_of_average("numbers.txt", 3)
    print(cubed_root)


main()
