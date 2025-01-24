"""
 Create a function update_frequencies() , that will do just that: receive a
 list containing an existing list of frequencies, as well as a string
 representing a new DNA sequence, and update the previous numbers to reflect
 their added frequencies. Your function program must also print the nucleotides
 being added to each frequency.

"""


def update_frequencies(old_frequencies, new_sequence):
    counts = [0] * len(old_frequencies)
    for i in range(len(old_frequencies)):
        string = old_frequencies[i][0]
        counts[i] = new_sequence.count(string)

    new_frequencies = [(old_frequencies[i][0], old_frequencies[i][1] + counts[i]) for i in range(len(old_frequencies))]

    return new_frequencies


def main():

    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)
    print(new_frequencies)


main()
