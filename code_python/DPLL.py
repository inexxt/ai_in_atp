import sys
from common import *
from copy import deepcopy

def DPLL(S: CNF, lits: LIT):
    # print("Call with ", len(lits), S, lits)
    prev_len = -1
    while prev_len != len(S):
        prev_len = len(S)
        S, lits = unit_clause(S, lits)        
        S, lits = pure_literal(S, lits)
        S, lits = tautology(S, lits)

    if not S:
        return "SAT"

    if check_for_empty(S):
        return "UNSAT"

    # splitting rule
    get_single = lambda s: next(iter(s))

    S2, lits2 = deepcopy(S), deepcopy(lits)
    x = get_single(lits2)
    S2.add(frozenset({x}))
    
    if DPLL(S2, lits2) == "SAT":
        return "SAT"

    S3, lits3 = deepcopy(S), deepcopy(lits)
    S3.add(frozenset({-x}))

    if DPLL(S3, lits) == "SAT":
        return "SAT"
    else:
        return "UNSAT"


def main(fname: str):
    num_lit, _, data = input_data(fname)
    available_lits = {abs(l) for C in data for l in C}
    res = DPLL(data, available_lits)
    print(res)

if __name__ == "__main__":
    main(sys.argv[1])