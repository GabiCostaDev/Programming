"""
Write a function called get_matryoshka_list() that will turn a list full of numbers into
a list of ascending lists, depending on its contents. Here's the algorithm:
- The program will traverse the list starting at index 0.
- The program will create a new temporary list for every section of the original list that includes numbers in ascending order.
- When a number is encountered that is not in ascending order compared to the number preceding it, no additional items will be added to the temporary list, and the temporary list will be added to a “repository” list.
- When the program reaches the end of the original list, the “repository” list of lists will be returned to the calling function.

"""


def get_matryoshka_list():


def main():

    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)
    print(matryoshka_list)


main()