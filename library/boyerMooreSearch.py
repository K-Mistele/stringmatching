def _badCharacterTable(str):
    print("Bad character table")

def _goodSuffixHeuristic():
    print("Good suffic heuristic")

def boyerMooreSearch(corpus, searchTerm):
    print(f'Using Boyer-Moore to search corpus for "{searchTerm}"')
    print(f'*********************************************************')

    # GRAB LENGTHS OF BOTH STRINGS FOR LOOP CONTROL
    corpusLength = len(corpus)
    searchTermLength = len(searchTerm)

    # TODO: FINISH ME