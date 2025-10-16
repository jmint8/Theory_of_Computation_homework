import random
#  Homework Random Name Generator
'''
G = (V, ∑, S, P)
V = {S, X, Y, Z}
∑ = { Adjectives, Nouns, and, the, of}
S = S
P = ({S -> The X},{X -> Y | Y of Z | Y and Y | Y and the Y},{Z -> Y | Y and Y | Y and the Y})


Y = nouns or adjective + noun
'''
def readfile(filename):
    f_in = open(filename, "r")
    list = f_in.readlines()
    for i in range(len(list)):
        list[i] = list[i].strip()
    f_in.close()
    return list

def read_files_intrinsic(adjectives, nouns):
    adj_list = readfile(adjectives)
    noun_list = readfile(nouns)
    return  noun_list, adj_list


# defining the grammar functions below
def S(noun_list, adj_list):
    return "The " + X(noun_list, adj_list)

def X(noun_list, adj_list):
    rand = random.randint(1,4)
    if rand == 1:
        return Y(noun_list, adj_list)
    elif rand == 2:
        return Y(noun_list,adj_list) + " of " + Z(noun_list,adj_list)
    elif rand == 3:
        return Y(noun_list,adj_list) + " and " + Y(noun_list,adj_list)
    else:
        return Y(noun_list,adj_list) + " and the " + Y(noun_list,adj_list)

def Z(noun_list,adj_list):
    rand = random.randint(1,3)
    if rand == 1:
        return Y(noun_list,adj_list)
    elif rand == 2:
        return Y(noun_list,adj_list) + " and " + Y(noun_list,adj_list)
    else:
        return Y(noun_list,adj_list) + " and the " + Y(noun_list,adj_list)

def Y(noun_list, adj_list):
    rand = random.randint(1,2)
    if rand == 1:
        return random.choice(noun_list)
    else:
        return random.choice(adj_list) + " " + random.choice(noun_list)

# recursion is nice
def generate_name(noun_list, adj_list):
    string = S(noun_list, adj_list) 
    return string


if __name__ == "__main__":
    def main():
        nouns = "nouns.txt"
        adjectives = "adjectives.txt"
        #noun_list,adj_list = read_files_intrinsic(adjectives,nouns)
        noun_list = readfile(nouns)
        adj_list = readfile(adjectives)

        gen_name = generate_name(noun_list,adj_list)
        print(gen_name)
        print("Goodbye!")
        return 0

main()