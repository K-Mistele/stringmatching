# MODULES
import argparse

# CUSTOM IMPORTS
from library.naiveSearch import  naiveSearch
from library.boyerMooreSearch import boyerMooreSearch

# ARGUMENT PARSING
def parseArgs():
    parser = argparse.ArgumentParser(description="Search for a string in the specified (ASCII) text file")
    parser.add_argument("filename", help="A string that specifies the name of the file containing the ASCII text to search through")
    parser.add_argument("searchTerm", help="The pattern to search for in the specified ASCII text file")
    args = parser.parse_args()

    return args.filename, args.searchTerm
# MAIN
def main():
    print("Hello world!")
    # GRAB THE PARSER ARGUMENTS
    textFileName, pattern = parseArgs()
    print(f'Received arguments textFileName: {textFileName} and pattern: {pattern}')

    with open(textFileName, 'r') as f:
        corpus = f.read()

    print(f'Length of corpus: {len(corpus)} characters')

    naiveSearch(corpus, pattern)
    boyerMooreSearch(corpus, pattern)


main()