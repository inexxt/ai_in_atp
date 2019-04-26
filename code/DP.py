import sys
from common import *


def resolution(S: CNF, lits: LIT):
    #  choose a literal l and split the set of clauses S into a
    #  set S1 of clauses containing l only positively, a set S2 of clauses containing l only
    #  negatively, and the rest S3, and a new set of clauses is {c1 sum c2 \ {l, -l} for c1, c2 in s1, s2} sum s3
    l = lits.pop()

    S1 = {C for C in S if l in C and -l not in C}
    S2 = {C for C in S if -l in C and l not in C}
    S3 = S - S1 - S2

    return {(c1 | c2) - {l, -l} for c1 in S1 for c2 in S2} | S3, lits


def DF(S: CNF, lits: LIT):
    
    while True:

        prev_len = -1
        while prev_len != len(S):
            prev_len = len(S)
            for method in [unit_clause, pure_literal, tautology]:

                S, lits = method(S, lits)
                
                if not S:
                    return "SAT"

                if check_for_empty(S):
                    return "UNSAT"

        print("S ", len(S), "lits ", len(lits))
        S, lits = resolution(S, lits)


def main(fname: str):
    num_lit, _, data = input_data(fname)

    res = DF(data, set(range(1, num_lit + 1)))
    print(res)


if __name__ == "__main__":
    main(sys.argv[1])