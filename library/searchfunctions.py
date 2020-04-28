
def naiveSearch(corpus, searchTerm):
    print(f'Searching corpus for {searchTerm}')
    corpusLength = len(corpus)
    searchTermLength = len(searchTerm)

    # CREATE ALIGNMENTS
    for i in range(0, corpusLength - searchTermLength + 1):
        # CREATE A POINTER FOR ALIGNMENTS. IT STARTS AT THE BEGINNING OF THE PATTERN, I.E. AT INDEX 0
        # IF THE FIRST CHARACTER OF THE ALIGNMENT MATCHES, KEEP INCREMENTING IT
        alignmentPointer = 0

        # USE THE ALIGNMENT POINTER TO CHECK THE ALIGNMENT
        alignmentFound = True

        while alignmentPointer < searchTermLength:
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
            print(f'Found an alignment at {i}!')


def boyerMooreSearch(corpus, searchTerm):
    print(f'Using Boyer-Moore to search corpus for {searchTerm}')