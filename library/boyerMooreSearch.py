# IMPORTS
import string

def _createBadCharacterTable(pattern):
    print("Building bad character table")

    # CREATE AN ALPHABET THAT IS ALL OF THE PRINTABLE STRING CHARACTERS
    alphabet = str(string.printable)
    alphabetSize = len(alphabet)

    # CREATE THE TABLE (dictionary) THAT STORES THE INDEX OF THE LAST OCURRENCE OF THE CHARACTER IN THE STRING
    table = {}
    i = 0
    for character in pattern:
        table[character] = i
        i += 1
    print(table)

def _goodSuffixHeuristic():
    print("Good suffic heuristic")

def boyerMooreSearch(corpus, searchTerm):
    print(f'Using Boyer-Moore to search corpus for "{searchTerm}"')
    print(f'*********************************************************')

    # GRAB LENGTHS OF BOTH STRINGS FOR LOOP CONTROL
    corpusLength = len(corpus)
    searchTermLength = len(searchTerm)

    # CREATE THE BAD CHARACTER TABLE
    badCharTable = _createBadCharacterTable(searchTerm)
    print(badCharTable)

    # TODO: FINISH ME