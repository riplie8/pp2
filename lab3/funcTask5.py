import itertools

def print_permutations():
    s = input("give a string: ")
    perms = itertools.permutations(s)
    for p in perms:
        print("".join(p))

print_permutations()
