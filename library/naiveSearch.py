
def naiveSearch(corpus, searchTerm):
    print(f'Searching corpus for "{searchTerm} with Naive Search"')
    print(f'******************************************************')

    # GRAB LENGTHS OF BOTH STRINGS FOR LOOP CONTROL
    corpusLength = len(corpus)
    searchTermLength = len(searchTerm)

    # CREATE ALIGNMENTS
    totalShifts = 0
    totalComparisons = 0
    for i in range(0, corpusLength - searchTermLength + 1):
        totalShifts += 1
        # CREATE A POINTER FOR ALIGNMENTS. IT STARTS AT THE BEGINNING OF THE PATTERN, I.E. AT INDEX 0
        # IF THE FIRST CHARACTER OF THE ALIGNMENT MATCHES, KEEP INCREMENTING IT
        alignmentPointer = 0

        # USE THE ALIGNMENT POINTER TO CHECK THE ALIGNMENT
        alignmentFound = True

        while alignmentPointer < searchTermLength:
            totalComparisons += 1
            # IF THE CHARACTER MATCHES, CHECK THE NEXT ONE IN THE ALIGNMENT
            if searchTerm[alignmentPointer] == corpus[i + alignmentPointer]:
                alignmentPointer += 1

            # OTHERWISE, BREAK AND MOVE TO THE NEXT ALIGNMENT
            else:
                alignmentFound = False
                break

        # IF AN ALIGNMENT WAS NOT FOUND, MOVE TO THE NEXT ALIGNMENT
        if not alignmentFound:
            continue

        # IF AN ALIGNENT WAS FOUND, PRINT IT!
        else:
            print(f'Found a match at shift {i}!')

    print(f'\nTotal shifts: {totalShifts}')
    print(f'Total comparisons: {totalComparisons}')
    print('\n\n')


