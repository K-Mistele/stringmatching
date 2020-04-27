# MODULES

# CUSTOM IMPORTS
from library.searchfunctions import  naiveSearch, boyerMooreSearch

# MAIN
def main():
    print("Hello world!")

    corpus = ""
    with open("corpus.txt", 'r') as f:
        corpus = f.read()

    print(f'Length of corpus: {len(corpus)} characters')

    naiveSearch(corpus, "mountain")
    boyerMooreSearch(corpus, "register")

main()