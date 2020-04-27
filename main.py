# IMPORTS

# MAIN
def main():
    print("Hello world!")

    corpus = ""
    with open("corpus.txt", 'r') as f:
        corpus = f.read()

    print(f'Length of corpus: {len(corpus)} characters')

main()