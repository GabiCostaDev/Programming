"""
Write a function get_word_count() that will accept the address of a txt file 
(a string) and will returns the number of words contained in this file. 

"""


def get_word_count(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

    text = file.read()
    word_count = text.count(' ') + 1
    file.close()

    return word_count


def main():
    count = get_word_count("voltaire.txt")
    print(f"This file has {count} word(s).")


main()












