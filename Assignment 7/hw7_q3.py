"""
Your function, create_error_log() would accept the DNA sequence and the
name of the indices file, and generate a report (i.e. a txt file called
error_log.txt ) of which indices are not valid.

"""


def create_error_log(dna_sequence, filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return f"FILENOTFOUNDERROR: The file specified was not found or could not be opened."
    line_num = 1
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        try:
            value = int(line)
            if value > len(dna_sequence):
                print(f"INDEXERROR at LINE {line_num}: The value read, {value}, is larger than the sequence length of {len(dna_sequence)}.")
        except ValueError:
            print(f"VALUEERROR at LINE {line_num}: The value read, {line}, cannot be casted into an integer to be used as an index.")
        line_num += 1
    file.close()


def main():
    create_error_log("ACTGC AXT", 'indices.txt')


main()





