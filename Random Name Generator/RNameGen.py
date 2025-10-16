#  Homework Random Name Generator
'''
G = (V, ∑, S, P)
V = {S, X, Y, Z}
∑ = { Adjectives, Nouns, and, the, of}
S = S
P = ({S -> The X},{X -> Y | Y of Z | Y and Y | Y and the Y},{Z -> Y | Y and Y | Y and the Y})
'''
def readfile(filename):
    f_in = open(filename)
    list = f_in.readlines()
    for i in range(len(list)):
        list[i] = list[i].strip()
    f_in.close()
    return list

def read_files_intrinsic(adjectives, nouns):
    adj_list = readfile(adjectives)
    noun_list = readfile(nouns)
        
    return  adj_list, noun_list
    
