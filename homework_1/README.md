# Artificial Intelligence in Theorem Proving
## Homework 1
---

### PART 1 
Implementation of DP and DPLL algorithms is done in Python, in `code_python/DP.py` and `code_python/DPLL.py`.
To run DPLL on example file, execute
```bash
python3 code_python/DPLL.py ex_sat.cnf
```

Testing is done in `test.sh` script, which:
 - Runs SAT tests for DPLL (flat30-60: 30 vertices, 60 edges - 100 instances, all satisfiable)
 - Runs UNSAT tests for DPLL (uuf50-218: 50 variables, 218 clauses - 1000 instances, all unsat)
 - Runs SAT/UNSAT tests for DP and DPLL, comparing their outputs

It is done this way, because our implementation of DP for some reason seems to very slow, and it prevents one from testing it on any of the *proper* datasets from SATLIB. So, we test it only on some small, artificially generated data, and assume that DPLL is the ground truth (because it was tested with proper data from SATLIB).

Concerning time and memory usage, our implementation of DPLL is comparably fast on small examples that both algorithms can evaluate. But, on larger examples (these taken from SATLIB), DP does not terminate and consumes all available memory, while DPLL takes about 0.04s and 1MB of memory (measured with `valgrind massif`), but comparing it across examples, it seems that most of it is memory allocated by python interpreter.


### PART 2

Part 2 is described in [here](http://localhost:8890/notebooks/PART_2a.ipynb)

