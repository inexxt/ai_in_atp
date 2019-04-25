#include <iostream>
#include <string>
#include <cassert>
#include <sstream>


using namespace std;

void unit_clause() {
    //  if there is some clause consisting of a single literal l (a
    // unit clause), remove instances of −l from other clauses and then remove any
    // clauses containing l (including the unit clause itself);
    return;
}

void pure_literal() {
    // if there is a literal appearing in the formula only positively
    // or only negatively, remove all clauses containing it;
    return;
}

void tautology() {
    //  if some clause contains complementary literals, l and −l,
    // remove this clause;
}

int main() {
    int num_clauses;
    int num_vars;

    string line, p, cnf;
    
    // comments section
    do {
        getline(cin, line);
    } while (line[0] == 'c');

    // metadata section
    istringstream iss(line);
    iss >> p >> cnf >> num_vars >> num_clauses;
    cout << "num_vars: " << num_vars << ", num_clauses: " << num_clauses << "\n";


    // data section
    vector<int> v[num_clauses];
    bool v[num_clauses]; //active clauses

    return 0;
}