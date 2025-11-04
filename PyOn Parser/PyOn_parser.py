#!/usr/bin/python3
#
# definition of Grammar for PyOn 
#
# S -> { X }
# X -> X , X | Y : Z 
# Y -> ""








DESCRIPTION = '''
A homebrew JSON parser which extends standard JSON with sets and complex numbers.
'''

import argparse
import os.path

YOUR_NAME_HERE = "Captain Jack Sparrow" # Replace this with your name.


def parse_file(file_name: str) -> dict:
    # Delete the "pass"placeholder below, and start coding!
    pass


def main():
    ap = argparse.ArgumentParser(description=(DESCRIPTION + f"\nBy: {YOUR_NAME_HERE}"))
    ap.add_argument('file_name', action='store', help='Name of the JSON file to read.')
    args = ap.parse_args()

    file_name = args.file_name
    local_dir = os.path.dirname(__file__)
    file_path = os.path.join(local_dir, file_name)

    dictionary = parse_file(file_path)

    print('DICTIONARY:')
    print(dictionary)


if __name__ == '__main__':
    main()