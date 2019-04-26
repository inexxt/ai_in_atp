#!/bin/bash
# set -e

IDX=1;
LEN=$( ls -1q data_sat/ | wc -l )

for fn in data_sat/*
do
    echo "phase 1/3 (testing DPLL on SAT) progress $IDX / $LEN";
    # echo $fn;     

    if [[ "$( python3 code_python/DPLL.py $fn )" == "UNSAT" ]] ; then
       echo "wrong";
       exit 1;
    fi

    IDX=$(( IDX + 1 )); 
done


IDX=1;
LEN=$( ls -1q small_data/ | wc -l )
for fn in data_unsat/* 
do
    echo "phase 2/3 (testing DPLL on UNSAT) progress $IDX / $LEN ";
    # echo $fn;

    if [[ $( python3 code_python/DPLL.py $fn ) == "SAT" ]] ; then
       echo "wrong";
       exit 1;
    fi

    # echo $fn; 
    IDX=$(( IDX + 1 )); 
done

IDX=1;
LEN=$( ls -1q small_data/ | wc -l )
for fn in small_data/* 
do
    echo "phase 3/3 (testing DP by DPLL) progress $IDX / $LEN";
    # echo $fn;

    out1="$( python3 code_python/DP.py $fn )";
    out2="$( python3 code_python/DPLL.py $fn )";
    
    # echo $out2;
    # echo $out1;

    if [[ $out1  != $out2 ]] ; then
       echo "wrong";
       exit 1;
    fi

    IDX=$(( IDX + 1 ));
done


echo "OK";

