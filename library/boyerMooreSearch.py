# IMPORTS
import string

# CREATE A TABLE THAT TELLS US HOW FAR TO SHIFT WHEN A MISMATCH HAPPENS BASED ON THE PATTERN
def _createBadCharacterHeuristicTable(searchTerm):
    print("Building bad character table")

    # CREATE AN ALPHABET THAT IS ALL OF THE PRINTABLE STRING CHARACTERS
    # SLICE 0 THROUGH UP TO THE 5TH FROM LAST CHARACTERS; OTHERS ARE TAB, NEWLINE, BYTES, ETC
    alphabet = str(string.printable[0:-5])
    alphabetSize = len(alphabet)

    # CREATE THE TABLE (dictionary) THAT STORES THE INDEX OF THE LAST OCURRENCE OF THE CHARACTER IN THE STRING
    table = {}
    i = 0

    # STORE THE LAST INDEX OF EACH CHARACTER IN THE PATTERN IN THE TABLE
    for character in searchTerm:
        table[character] = i
        i += 1

    # FOR ALL OTHER CHARACTERS IN THE ALPHABET, STORE A -1
    for character in alphabet:
        if character not in table:
            table[character] = -1


    # RETURN THE DICTIONARY
    return table

def _createGoodSuffixHeuristicTable(searchTerm):
    print("Building good suffix table")

    # BUILD AN ARRAY shiftDistance WHERE EACH ENTRY shiftDistance[i] CONTAINS THE SHIFT DISTANCE OF THE PATTERN
    # IF A MISMATCH AT POSITION I - 1 IN THE PATTERN OCCURS

    # THE FIRST GOOD-SUFFIX HEURISTIC - DOES THE MATCHING SUFFIX OCCUR SOMEWHERE ELSE IN THE PATTERN?
    # BUILD TWO TABLES: F (USED FOR CALCULATING shiftDistance) AND shiftDistance, DISCUSSED ABOVE
    i = len(searchTerm)
    j = i + 1
    f = [0] * j # f[i] = n, n IS THE STARTING POSITION OF THE WIDEST BORDER OF THE SUFFIX STARTING AT POSITION i
    shiftDistance = [0] * j # shiftDistance[j] = x, x IS THE SHIFT DISTANCE IF A BORDER CAN'T BE EXTENDED TO THE LEFT
    f[i] = j
    while (i) > 0:
        while (j <= len(searchTerm)) and not (searchTerm[i - 1] == searchTerm[j - 1]):
            if shiftDistance[j] == 0:
                shiftDistance[j] = j - i
            j = f[j]
        i -= 1
        j -= 1
        f[i] = j

    ## THE SECOND GOOD-SUFFIX HEURISTIC: DOES THE MATCHING SUFFIX CONTAIN A MATCH TO A PREFIX?
    j = f[0]
    i = 0
    while i <= len(searchTerm):
        if shiftDistance[i] == 0:
            shiftDistance[i] = j
        if i == j:
            j = f[j]
        i += 1

    return shiftDistance



def boyerMooreSearch(corpus, searchTerm):
    print(f'Using Boyer-Moore to search corpus for "{searchTerm}"')
    print(f'*********************************************************')

    # GRAB LENGTHS OF BOTH STRINGS FOR LOOP CONTROL
    corpusLength = len(corpus)
    searchTermLength = len(searchTerm)

    # CREATE THE BAD CHARACTER TABLE
    badCharTable = _createBadCharacterHeuristicTable(searchTerm)
    goodSuffixTable = _createGoodSuffixHeuristicTable(searchTerm)

    # TODO: FINISH ME
    # TODO: RIGHT NOW, I AM ONLY USING THE BAD CHAR RULE

    shift = 0
    totalShifts = 0
    # LOOP UNTIL WE HAVE SHIFTED THE SEARCH TERM TO BE ALIGNED WITH THE LAST CHARACTERS OF THE CORPUS TEXT
    while (shift + searchTermLength <= corpusLength ):
        totalShifts += 1
        # BECAUSE WE ARE ITERATING FROM LEFT TO RIGHT, WE WILL START AT THE RIGHTMOST CHARACTER WITH HAS INDEX len(str)-1
        # AND THEN DECREMENT IT AS WE ITERATE TO THE LEFT UNTIL IT REACHES 0
        print(corpus)
        print(" " * shift + searchTerm)

        indexInTerm = searchTermLength - 1
        matchFound = True
        # LOOP ACROSS THE ALIGNMENT FROM RIGHT TO LEFT
        while indexInTerm >= 0:

            # IF THE CHARACTERS MATCH, CONTINUE SO THAT WE CHECK THE ONES TO THE LEFT
            if searchTerm[indexInTerm] == corpus[shift + indexInTerm]:
                indexInTerm -= 1

            # IF A MATCH WAS NOT FOUND, BREAK EARLY AND SHIFT
            else:
                matchFound = False
                break

        # IF A MATCH WAS FOUND, PRINT ITS LOCATION

        if matchFound:
            print(f'Match found at shift = {shift}')
            print(corpus)
            print(" " * shift + searchTerm)

            # PREVENT OUT-OF-BOUNDS READ
            if shift + searchTermLength == corpusLength:
                break

            nextShift = goodSuffixTable[0]
        else:

            # SHIFT THE PATTERN SO THAT THE NEXT ALIGNMENT HAS THE CHARACTER IN THE CORPUS THAT BROKE THE POTENTIAL MATCH
            # BE ALIGNED WITH ITS LOCATION IN THE PATTERN, OTHERWISE, JUST SHIFT THE PATTERN BY ONE

            # IF A MATCH IS NOT FOUND, WE TAKE THE MAXIMUM OF THE NEXT SHIFTS CALCULATED BY EACH HEURISTIC
            locOfBadCharInSearchTerm = indexInTerm
            nextShiftBadChar = max(1, locOfBadCharInSearchTerm - badCharTable[corpus[shift+locOfBadCharInSearchTerm]])
            nextShiftGoodChar = goodSuffixTable[locOfBadCharInSearchTerm + 1]
            nextShift = max(nextShiftBadChar, nextShiftGoodChar)

        shift += nextShift
    print(f'\nTotal Shifts: {totalShifts}')