# MODULES

# CUSTOM IMPORTS
from library.naiveSearch import  naiveSearch
from library.boyerMooreSearch import boyerMooreSearch

# MAIN
def main():
    # TODO: FIND A BETTER WAY TO PROCESS INPUTS & ARGUMENTS
    print("Hello world!")

    with open("corpus.txt", 'r') as f:
        corpus = f.read()

    # TODO THIS IS JUST FOR DEBUGGING
    corpus = "ATAGCCAGCATTTAGCCAGCAGCA"
    print(f'Length of corpus: {len(corpus)} characters')

    naiveSearch(corpus, "CAGCA")
    boyerMooreSearch(corpus, "CAGCA")


main()