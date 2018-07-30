def allTheNotes():
    ##    Number of strings
    stringNum = 6
    ##    Number of frets
    ##    fretNum = 12
    fretNum = 22
    ##    Size of matrix holding all notes
    noteNum = stringNum * fretNum

    ##    Notes
    ##    low_e_string_notes = ('E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3')
    ##    A_string_notes = ('A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3')
    ##    D_string_notes = ('D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4')
    ##    G_string_notes = ('G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4')
    ##    B_string_notes = ('B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4')
    ##    high_E_string_notes = ('E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5')

    low_e_string_notes = (
    'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3',
    'A#3', 'B3', 'C4', 'C#4', 'D4')
    A_string_notes = (
    'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4',
    'D#4', 'E4', 'F4', 'F#4', 'G4')
    D_string_notes = (
    'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4',
    'G#4', 'A4', 'A#4', 'B4', 'C5')
    G_string_notes = (
    'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5',
    'C#5', 'D5', 'D#5', 'E5', 'F5')
    B_string_notes = (
    'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5',
    'F5', 'F#5', 'G5', 'G#5', 'A5')
    high_E_string_notes = (
    'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5',
    'A#5', 'B5', 'C6', 'C#6', 'D6')

    ##     x defines the number of elements in each tuple, e.g. (x, y, note) where x is the
    ##     fret number, y is the string number, and note is the note at that point
    x = list(range(1, 4))

    ##     y is used as an index value
    y = list(range(0, noteNum + stringNum))
    ##     w, h are dimensions of x and y
    w, h = len(x), len(y);
    ##     z is an empty matrix of tuples the size as defined due to the number of strings and frets
    z = [[0 for x in range(w)] for y in range(h)]

    ##     ii is for indexing
    ii = 0
    ##     j is for indexing
    j = 1
    ##    This loop assigns grid references and notes to the matrix for each note
    while j < stringNum + 1:
        i = 0
        while i < fretNum + 1:
            z[ii][0] = y[i]
            z[ii][1] = j
            if j == 6:
                z[ii][2] = low_e_string_notes[i]
            elif j == 5:
                z[ii][2] = A_string_notes[i]
            elif j == 4:
                z[ii][2] = D_string_notes[i]
            elif j == 3:
                z[ii][2] = G_string_notes[i]
            elif j == 2:
                z[ii][2] = B_string_notes[i]
            elif j == 1:
                z[ii][2] = high_E_string_notes[i]
            i = i + 1
            ii = ii + 1
        j = j + 1

    return z





def findNoteLocations(note, z):

    noteLocations = []

    ##    this loop finds the tuples associated with a note and creates a list of all matching tuples
    i = 0
    while i < len(z):
        if note in z[i]:
            noteLocations.append(z[i])
        i = i + 1

    return noteLocations


##finds the shortest distance between two sets of x and y coordinates
def distanceFormula(a, b):
    a = [x for x in a[0:2]]
    b = [x for x in b[0:2]]

    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance


##  this function iterates through all combinations of note placements on the neck and
##  finds the two note combination with the shortest distance between them

def closestDistanceBetweenTwoNotes(a, b):
    ##    sets distance to an arbitrarily high value
    ##    distance returns the distance, plus the tuples of both notes
    ##    the tuples contain the fret, string, and note name of each note
    distance = [1000, 0, 0]

    a_numberOfPositions = len(a)
    b_numberOfPositions = len(b)

    i = 0
    j = 0
    while i < a_numberOfPositions:
        j = 0
        while j < b_numberOfPositions:
            ##            this calls the function to measure the distance between the notes
            x = distanceFormula(a[i], b[j])
            ##            print("the notes are ", a[i], " and ",b[j])
            ##            print("distance between notes is ", round(x,2))
            ##            this ensures that the smallest distance is the returned value
            if (x < distance[0]):
                distance = [x, a[i], b[j]]
            j = j + 1
        i = i + 1

        distance[0] = round(distance[0])

    return distance


# def closestMelodyNotesDistance(testNotes):
#     ##    This function locates all the places on the neck where a note can be played.
#     ##    It then takes the first two notes and finds the minimum distance between them,
#     ##    considering all the places on the neck where they could be played.
#     ##    Using the first pair of notes as a starting point, the next pair is then decided
#     ##    based on the previous value.  In this way, the closest distance is chosen, based
#     ##    on the preceding choice.
#
#     ##    I think this is called a Greedy Algorithm.  The following definition is from Wikipedia:
#
#     ##    A greedy algorithm is an algorithmic paradigm that follows the problem solving
#     ##    heuristic of making the locally optimal choice at each stage with the intent of
#     ##    finding a global optimum.
#
#     noteLocations = [[]]
#
#     ## Creates an array of all the notes' locations
#     g = 0
#     while g < len(testNotes):
#         noteLocations.append([])
#         noteLocations[g] = findNoteLocations(testNotes[g])
#         g = g + 1
#
#     ##  Finds the closest distance between every pair of notes
#     notePairs = [[]]
#     notePairs[0] = closestDistanceBetweenTwoNotes(noteLocations[0], noteLocations[1])
#     d = 1
#     while d < len(testNotes) - 1:
#         notePairs.append(closestDistanceBetweenTwoNotes([notePairs[d - 1][2]], noteLocations[d + 1]))
#         d = d + 1
#
#     ##  This adds all the individual note pairs to one array
#     testNotesClosestLocations = notePairs[0][1:3]
#     d = 1
#     while d < len(testNotes) - 1:
#         testNotesClosestLocations.append(notePairs[d][2])
#         d = d + 1
#
#     return testNotesClosestLocations


def printToTab(testNotesClosestLocations):
    import numpy as np
    from astropy.io import ascii
    from astropy.table import Table, Column, MaskedColumn

    StringNames = np.array(['E', 'B', 'G', 'D', 'A', 'e'])
    bar = np.array(['|', '|', '|', '|', '|', '|'])
    ##  this dash array is the default empty column.  It needs to have two dashes to allow
    ##  space for a number with two digits.  If there is only one dash, only one of the
    ##  two digits will be stored
    dash = np.array(['--', '--', '--', '--', '--', '--'])

    ##  this loop fills the tab with empty notes as a placeholder where the actual
    ##    notes are subsequently entered
    notesOnTab = [dash]
    a = 0
    while a < len(testNotesClosestLocations) - 1:
        notesOnTab.append(dash)
        a = a + 1

    ##  converts the array notesOnTab from a list of arrays to a numpy array
    numpyNotes = np.array(notesOnTab)

    ## this loop takes the coordinates listed in each note's tuple and maps them to the correct
    ##    place on the tab, and updates the empty numpty notes array with the notes
    j = 0
    while j < len(testNotesClosestLocations):
        k = 0
        ##  6 is the number of strings
        while k < 6:
            if testNotesClosestLocations[j][1] == k + 1:
                ##            if the value to be stored has only a single digit, it is buffered with a dash
                ##            as there is space for two characters to allow for double digit numbers.
                ##            this is mostly a formatting thing so that all the numbers will be vertically
                ##            aligned
                if len(str(testNotesClosestLocations[j][0])) == 1:
                    numpyNotes[j][k] = str(testNotesClosestLocations[j][0]) + '-'
                elif len(str(testNotesClosestLocations[j][0])) == 2:
                    numpyNotes[j][k] = str(testNotesClosestLocations[j][0])
                break
            k = k + 1
        j = j + 1

    ##  the tab is printed by adding on columns to a table and then printing a table
    ##
    tabContents = [StringNames, bar, dash]
    a = 0
    while a < len(testNotesClosestLocations):
        tabContents.append(numpyNotes[a])
        tabContents.append(dash)
        a = a + 1
    tabContents.append(bar)

    ##  this commented section will print the tab to a .txt file
    tab = Table(tabContents)
    ##ascii.write(tab, 'tab.txt',overwrite=True)

    #  this prints to the Shell
    import sys
    print('\n')
    ascii.write(tab, sys.stdout)

    return




