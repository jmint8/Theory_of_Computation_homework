#!/usr/bin/python3
#
# definition of Grammar for PyOn 
# non-terminals are represented by uppercase letters
# S is the staring state. X represents an object. Y represents a key. Z represents a value.
# L represents a list. V represents values. O represents an object. I represents an integer.
# F represents a float. B represents a boolean. W represents a string. C represents characters. G represents a group of digits. 
# T represents a sign. R represents + or -. H represents a number (integer or float). N represents a number. 
# J represents a complex number. Q represents the form of floats.
"""
Grammar for PyOn Parser
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
import re
import sys

YOUR_NAME_HERE = "Mitchel" # Replace this with your name.

TOKE_DEX = [
    ('COMPLEX', r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?[-\+](\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?i|[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?i'),
    ('NUMBER',  r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'),
    ('STRING',  r'"([^"\\]*(\\.[^"\\]*)*)"'),
    ('TRUE',    r'true|True'),
    ('FALSE',   r'false|False'),
    ('NULL',    r'null'),
    ('LBRACE',  r'\{'),
    ('RBRACE',  r'\}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('COLON',   r':'),
    ('COMMA',   r','),
    ('SKIP',    r'[ \t\n\r]+'),
    ('MISMATCH',r'.'),
]
# Toke dex, get it, like Pokédex but for... tokens. haha.  this is additional info on regex formating: https://www.keycdn.com/support/regex-cheat-sheet, very useful 
# order matters here, so put longer patterns first
# COMPLEX must come before NUMBER to avoid partial matches
# STRING must come before TRUE, FALSE, NULL to avoid partial matches
# SKIP must come before MISMATCH to avoid matching whitespace as a mismatch

class Token:
    def __init__(self, type, val, pos):
        self.type = type
        self.value = val
        self.pos = pos
    def __repr__(self):
        return f'Token({self.type}, {repr(self.val)})'
    
def tokenize(text):
    token_specification = TOKE_DEX
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    get_token = re.compile(tok_regex).match
    pos = 0
    tokens = []
    gt = get_token(text)
    while gt is not None:
        type = gt.lastgroup
        if type == 'SKIP':
            pass
        elif type == 'MISMATCH':
            raise SyntaxError(f'Unexpected character')
        else:
            val = gt.group(type)
            tokens.append(Token(type, val, pos))
        pos = gt.end()
        gt = get_token(text, pos)
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_object()

    def parse_object(self):
        obj = {}
        self.expect('LBRACE')
        if self.peek().type != 'RBRACE':
            while True:
                key = self.parse_string()
                self.expect('COLON')
                value = self.parse_value()
                obj[key] = value
                if self.peek().type == 'COMMA':
                    self.expect('COMMA')
                else:
                    break
        self.expect('RBRACE')
        return obj

    def parse_array(self):
        arr = []
        self.expect('LBRACKET')
        if self.peek().type != 'RBRACKET':
            while True:
                value = self.parse_value()
                arr.append(value)
                if self.peek().type == 'COMMA':
                    self.expect('COMMA')
                else:
                    break
        self.expect('RBRACKET')
        return arr

    def parse_value(self):
        token = self.peek()
        if token.type == 'LBRACE':
            return self.parse_object()
        elif token.type == 'LBRACKET':
            return self.parse_array()
        elif token.type == 'STRING':
            return self.parse_string()
        elif token.type == 'NUMBER':
            return self.parse_number()
        elif token.type == 'COMPLEX':
            return self.parse_complex()
        elif token.type == 'TRUE':
            self.expect('TRUE')
            return True
        elif token.type == 'FALSE':
            self.expect('FALSE')
            return False
        elif token.type == 'NULL':
            self.expect('NULL')
            return None
        else:
            raise SyntaxError(f'Unexpected token: {token}')
        
    def parse_string(self):
        token = self.expect('STRING')
        return bytes(token.value[1:-1])
    
    def parse_number(self):
        token = self.expect('NUMBER')
        if '.' in token.value or 'e' in token.value or 'E' in token.value:
            return float(token.value)
        else:
            return int(token.value)
        
    def parse_complex(self):

        # okay this will be fun 
        pass

def parse_file(file_name: str) -> dict:
    f_in = open(file_name, 'r')
    text = f_in.read()
    f_in.close()
    tokens = tokenize(text)
    parser = Parser(tokens)
    return parser.parse()

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