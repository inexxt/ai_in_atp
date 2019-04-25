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


def check_for_empty(S: CNF):
    return any(not C for C in S)


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
