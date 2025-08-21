from molecular_threeSAT_solver import MolecularThreeSATSolver

def test_molecular_sat():  # Create a simple satisfiable 3-SAT formula
    solver = MolecularThreeSATSolver(2)  # Using 2 variables for a simpler example
    
    # Add a simple clause: (x1 ∨ x2)
    solver.add_clause([1, 2, 1])  # Using x2 twice to make it a 3-literal clause
    
    print("\nSolving formula...")
    result = solver.solve()
    print(f"\nFormula is {'satisfiable' if result else 'unsatisfiable'}")

if __name__ == "__main__":
    test_molecular_sat()