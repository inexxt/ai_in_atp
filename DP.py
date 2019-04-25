from typing import Set
import sys

CNF = Set[Set[int]]
LIT = Set[int]


def remove_lits(S: CNF, lits_to_remove: LIT):
    for C in S:
        if C & lits_to_remove:
            S.remove(C)
            S.add(C - lits_to_remove)


def unit_clause(S: CNF, lits: LIT):
    #   if there is some clause consisting of a single literal l (a
    #  unit clause), remove instances of −l from other clauses and then remove any
    #  clauses containing l (including the unit clause itself);
    get_single = lambda C: next(iter(C))

    singles = {get_single(C) for C in S if len(C) == 1}
    remove_lits(S, {-l for l in singles})
    
    return {C for C in S if not (singles & C)}, lits - singles
    

def pure_literal(S: CNF, lits: LIT):
    #  if there is a literal appearing in the formula only positively
    #  or only negatively, remove all clauses containing it

    sign = lambda x: 1 if x >= 0 else 0

    counts = {l: [0, 0] for l in lits}
    for C in S:
        for l in C:
            counts[abs(l)][sign(l)] += 1

    lits_to_remove = {l for l, c in counts.items() if c[0] == 0 or c[1] == 0}

    remove_lits(S, lits_to_remove)
    return S, lits - lits_to_remove


def tautology(S: CNF, lits: LIT):
    #  if some clause contains complementary literals, l and −l,
    #  remove this clause;
    duplicates = lambda C: any(-l in C for l in C)
    return {C for C in S if not duplicates(C)}, lits


def resolution(S: CNF, lits: LIT):
    #  choose a literal l and split the set of clauses S into a
    #  set S1 of clauses containing l only positively, a set S2 of clauses containing l only
    #  negatively, and the rest S3, and a new set of clauses is {c1 sum c2 \ {l, -l} for c1, c2 in s1, s2} sum s3
    l = lits.pop()

    S1 = {C for C in S if l in C and -l not in C}
    S2 = {C for C in S if -l in C and l not in C}
    S3 = S - S1 - S2

    return {(c1 | c2) - {l, -l} for c1 in S1 for c2 in S2} | S3, lits


def check_for_empty(S: CNF):
    return any(not C for C in S)


def DF(S: CNF, lits: LIT):
    rules = [unit_clause, pure_literal, tautology, resolution]

    idx = 0
    while True:

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

        print("It " , idx, "Rule ", rules[idx % len(rules)], "S ", len(S), "lits ", len(lits))
        S, lits = rules[idx % len(rules)](S, lits)
        
        idx = idx + 1

def input_data(fname: str):
    with open(fname, "r") as f:
        lines = f.readlines()
    
    meta_loc = 0
    for e, l in enumerate(lines):
        if l[0] == "p":
            meta_loc = e

    meta = lines[meta_loc]
    # being careful about the last "0"s
    data = {frozenset(int(x) for x in l.split()[:-1]) for l in lines[meta_loc+1:]}

    p, cnf, num_lit, num_clauses = meta.split()
    
    assert(p == "p")
    assert(cnf == "cnf")

    num_lit = int(num_lit)
    num_clauses = int(num_clauses)

    return num_lit, num_clauses, data


def main(fname: str):
    num_lit, _, data = input_data(fname)

    res = DF(data, set(range(1, num_lit + 1)))
    print(res)

if __name__ == "__main__":
    main(sys.argv[1])