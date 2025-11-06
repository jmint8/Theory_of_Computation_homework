#!/usr/bin/python3
#
# definition of Grammar for PyOn 
# non-terminals are represented by uppercase letters
# S is the staring state. X represents an object. Y represents a key. Z represents a value.
# L represents a list. V represents values. O represents an object. I represents an integer.
# F represents a float. B represents a boolean. W represents a string. C represents characters. G represents a group of digits. 
# T represents a sign. R represents + or -. H represents a number (integer or float). N represents a number. 
# J represents a complex number. Q represents the form of floats.
# 
"""


# S -> { X }
# X -> X , X | Y : Z 
# Y -> w
# Z -> L | O | I | F | B | W
# L -> [ V ]
# V -> V , V | Z | ε
# O -> { X }
# W -> "C"
# B -> true | false
# I -> TG
# C -> aC | bC | cC |... | AC |... | ZC | ε
# G -> 0G |... | 9G | ε
# F -> TQ
# Q -> G.G | G.GeTG
# J -> Ni | NRHi
# H -> G | Q
# N -> TG | TQ
# T -> R | ε
# R -> + | -
"""


DESCRIPTION = ''' A homebrew JSON parser which extends standard JSON with sets and complex numbers. '''


import argparse
import os.path

YOUR_NAME_HERE = "Mitchel" # Replace this with your name.


def parse_file(file_name: str) -> dict:
    # Delete the "pass"placeholder below, and start coding!
    pass


def main():
    ap = argparse.ArgumentParser(description=(DESCRIPTION + f"\nBy: {YOUR_NAME_HERE}"))
    ap.add_argument('file_name', action='store', help='Name of the JSON file to read')
    args = ap.parse_args()

    file_name = args.file_name
    local_dir = os.path.dirname(__file__)
    file_path = os.path.join(local_dir, file_name)

    dictionary = parse_file(file_path)

    print('DICTIONARY:')
    print(dictionary)


if __name__ == '__main__':
    main()