from functions import findNoteLocations
from functions import distanceFormula
##from functions import closestDistanceBetweenTwoNotes
from functions import printToTab
from functions import allTheNotes

# from functions import closestMelodyNotesDistance


# two octave C major scale
testNotes = ('C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5')

z = allTheNotes()


def closestMelodyNotesDistance(testNotes):
    noteLocations = [[]]

    # Creates an array of all the notes' locations
    g = 0
    while g < len(testNotes):
        noteLocations.append([])
        noteLocations[g] = findNoteLocations(testNotes[g], z)
        g = g + 1

    ##   print(noteLocations)

    #  Finds the closest distance between every pair of notes
    notePairs = [[]]
    notePairs[0] = closestDistanceBetweenTwoNotes(noteLocations[0], noteLocations[1])
    d = 1
    while d < len(testNotes) - 1:
        notePairs.append(closestDistanceBetweenTwoNotes([notePairs[d - 1][2]], noteLocations[d + 1]))
        d = d + 1

    #  This adds all the individual note pairs to one array
    testNotesClosestLocations = notePairs[0][1:3]
    d = 1
    while d < len(testNotes) - 1:
        testNotesClosestLocations.append(notePairs[d][2])
        d = d + 1

    return testNotesClosestLocations


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


testNotesClosestLocations = closestMelodyNotesDistance(testNotes)

printToTab(testNotesClosestLocations)

