"""
Write a function, get_chord_dictionary() , that accepts the chord dataset's filepath (a string)
 as its only parameter and returns a dictionary.

"""
import csv
# chord_dict = {
#     ('A', 'C#', 'E', 'F#'): ['A6', 'A13'],
#     ('G#', 'D#', 'F#', 'C#', 'F', 'C', 'A#'): ['G#13'],
#     ('C#', 'E', 'G#'): ['C#m'],
#     ('E', 'G#', 'B'): ['Emaj', 'E6', 'E9', 'E13']
# }
#
# file = open('file.txt', 'r')
# lines = file.readlines()
#
# for line in lines:
#     notes = line.strip().split(',')
#     for chord_notes, chord_names in chord_dict.items():
#         if set(notes) == set(chord_notes):
#             print(','.join(chord_names))
#             break
#     else:
#         print('No potential chords found for: {}'.format(line.strip()))
#
# file.close()


def get_chord_dictionary(filename):
    chord_dict = {}
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        row = line.strip().split(',')
        note, chord_type, *notes = row
        if note not in chord_dict:
            chord_dict[note] = {}
        chord_dict[note][chord_type] = tuple(notes)

    return chord_dict

"""
Write a function get_possible_chords() that does just this: accept a list of notes (string objects) 
and a chord dictionary like the one returned by get_chord_dictionary() and returns a tuple of chords 
from the chord dictionary that this list of notes could satisfy. 

"""

def get_possible_chords(notes, chord_dict):
    possible_chords = []
    for chord, notes_tuple in chord_dict.items():
        if set(notes).issubset(set(notes_tuple)):
            possible_chords.append(chord)
    return tuple(possible_chords)

"""
Let's put our two functions from above together. Write a function get_chord_progression() that accepts 
two strings: 

- The first string represents the address for a CSV file that contains the chord progression of a song 
broken down into notes.
- The second string represents the address for the CSV file we'll use to create our chord dictionary. 

Using these two files and our functions get_chord_dictionary() and get_possible_chords(), 
get_chord_progression() must return a list of tuples, one tuple per chord in the chord progression file, 
where each tuple contains the chords from the chord dictionary that those notes could satisfy.

"""
def get_chord_progression(chord_prog_file, chords_file):
    chord_dict = get_chord_dictionary(chords_file)
    file = open(chord_prog_file, "r")
    chord_progression = []
    for line in file:
        notes = line.strip().split(",")
        possible_chords = get_possible_chords(notes, chord_dict)
        chord_progression.append(tuple(possible_chords))
    file.close()
    return chord_progression

"""
Write a function write_progression_file() that accepts a chord progression list like the one returned by 
get_chord_progression() and writes a file like the one in figure 2. That is, it writes one CSV line per tuple. 
Your function must also accept a string denoting the name of the file that write_progression_file() will create.
 
"""

def write_progression_file(chord_progression, filename):
    f = open(filename, 'w', newline='')
    writer = csv.writer(f)
    for chord_tuple in chord_progression:
        writer.writerow(chord_tuple)
    f.close()