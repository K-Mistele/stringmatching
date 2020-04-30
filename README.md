# String Matching
This project implements two approaches to the classic problem
of string matching: the classic "naive" approach, and the Boyer-Moore algorithm.

When a text file and search term are specified with the command line arguments, 
searches will be performed using both algorithms, and then various performance metrics will be compared.

## Running the Project
Command-line arguments are parsed with Python's `argparse` module for ease of development.
This project requires two main arguments:
* the name of an ASCII text file containing the text to be searched through
* the patternto search for in the text file

Format:
```shell script
python main.py someTextFile someSearchPattern
```

Example:
```shell script
python main.py genetic_code.txt ggaatcagagagcg
```

## Important Notes

This project is written in Python 3.7. If you have multiple versions of python installed,
you may need to specify your Python executable like so:
```shell script
python3 main.py genetic_code.txt ggaatcagagagcg
```

This code is guaranteed to work with more recent versions of Python (3.8), but no guarantee
of backwards compatibility is provided.
That being said, I expect that it would likely work with Python 3.6

## Installing Dependencies
Dependencies are managed with pip. To install dependencies, run:
```shell script
pip install -r requirements.txt
```