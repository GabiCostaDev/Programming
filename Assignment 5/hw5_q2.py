"""
Given two DNA sequences represented as string values, write a program that will:
- Fuse the two sequences by adding a nucleotide from each in alternating order
(i.e. ACT + CA = ACCAT). If any invalid nucleotides (i.e., not A , C , T , or G )
are found in either sequence, you should not include them in the fused sequence.
Instead, just keep track of how many of those invalid nucleotides you encountered.
- Create a complement sequence from the new, fused sequence. (i.e ACCAT complements to TGGTA)
- Print that complement sequence, as well all the amount of invalid nucleotides that we encountered.

"""

sequence_1 = input('Enter a DNA sequence: ')
sequence_2 = input('Enter a second DNA sequence: ')

invalid = 0
final = ''

for i in range(max(len(sequence_1), len(sequence_2))):
    if i < len(sequence_1):
        final += sequence_1[i]
    if i < len(sequence_2):
        final += sequence_2[i]

fused_final = ''

for i in range(len(final)):
    if final[i] == 'A':
        fused_final += 'T'
    elif final[i] == 'C':
        fused_final += 'G'
    elif final[i] == 'T':
        fused_final += 'A'
    elif final[i] == 'G':
        fused_final += 'C'
    else:
        invalid += 1
        fused_final += ''

print('Fused sequence: ', end='')

for i in range(len(fused_final)):
    if i < len(fused_final):
        print(fused_final[i], end='')

print(' ', end='')
print('| Invalid characters:', invalid)


