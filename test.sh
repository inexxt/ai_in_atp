#!/bin/bash

IDX=1; 
for fn in `ls data_sat`; 
    do; 
    python code/DPLL.py data3/$fn;
    echo $IDX;
    echo $fn; 
    IDX=$(( IDX + 1 )); 
done;


IDX=1;
for fn in `ls data_unsat`; 
    do; 
    python code/DPLL.py data3/$fn;
    echo $IDX;
    echo $fn; 
    IDX=$(( IDX + 1 )); 
done;