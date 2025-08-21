import random
import itertools
from dna_sequence import DNASequence
from molecular_tube import MolecularTube
from typing import List, Set, Dict, Optional

class MolecularThreeSATSolver:
    """Solves 3-SAT problems using molecular computing simulation."""
    
    def __init__(self, num_variables: int):
        self.num_variables = num_variables
        self.variable_encodings: Dict[int, str] = {}
        self.clauses: List[List[int]] = []
        self._initialize_encodings()
    
    def _initialize_encodings(self) -> None:
        """Initialize DNA encodings for variables and their negations."""
        bases = ['A', 'C', 'G', 'T']
        used_sequences: Set[str] = set()
        
        for var in range(1, self.num_variables + 1):
            # Generate positive literal encoding
            while True:
                pos_seq = ''.join(random.choices(bases, k=3))
                if self._is_valid_sequence(pos_seq, used_sequences):
                    break
            
            # Generate negative literal encoding
            while True:
                neg_seq = ''.join(random.choices(bases, k=3))
                if self._is_valid_sequence(neg_seq, used_sequences):
                    break
            
            self.variable_encodings[var] = pos_seq
            self.variable_encodings[-var] = neg_seq
            
            # Add sequences and their complements to used sequences
            used_sequences.add(pos_seq)
            used_sequences.add(DNASequence._generate_complementary_strand(pos_seq))
            used_sequences.add(neg_seq)
            used_sequences.add(DNASequence._generate_complementary_strand(neg_seq))

            
            print(f"Variable {var}:")
            print(f"  Positive: {pos_seq}")
            print(f"  Negative: {neg_seq}")
    
    def _is_valid_sequence(self, seq: str, used_sequences: Set[str]) -> bool:
        """Check if a sequence is valid and unique."""
        if seq in used_sequences:
            return False
        complement = DNASequence._generate_complementary_strand(seq)
        if complement in used_sequences:
            return False
        # Additional checks for sequence uniqueness
        for used_seq in used_sequences:
            if self._are_sequences_similar(seq, used_seq):
                return False
        return True
    
    def _are_sequences_similar(self, seq1: str, seq2: str) -> bool:
        """Check if sequences are too similar (to avoid false positives)."""
        return seq1 == seq2 or DNASequence._generate_complementary_strand(seq1) == seq2
    

    def add_clause(self, literals: List[int]) -> None:
        """Add a clause to the formula."""
        if len(literals) != 3:
            raise ValueError("Each clause must contain exactly 3 literals")
        if not all(-self.num_variables <= lit <= self.num_variables and lit != 0 for lit in literals):
            raise ValueError("Invalid literal value")
        self.clauses.append(literals)
    
    def _generate_initial_tube(self) -> MolecularTube:
        """Generate initial tube with all possible assignments."""
        tube = MolecularTube("T0")
        
        # Generate all possible assignments
        for assignment in itertools.product([False, True], repeat=self.num_variables):
            sequence = ""
            for var, value in enumerate(assignment, 1):
                sequence += self.variable_encodings[var if value else -var]
            molecule = DNASequence(sequence)
            tube.add(molecule)
            print(f"Generated molecule: {molecule.sequence}")
        
        return tube
    
    def _process_clause(self, tube: MolecularTube, clause: List[int]) -> MolecularTube:
        """Process a single clause using molecular operations."""
        result = MolecularTube(f"clause_{clause}")
        
        for molecule in tube.molecules:
            # Check if molecule satisfies any literal in the clause
            satisfies_clause = False
            
            for literal in clause:
                var_idx = abs(literal) - 1 # get the index
                pos = var_idx * 3   # get the correct position to check
                target_seq = self.variable_encodings[literal]
                
                if molecule.sequence[pos:pos + 3] == target_seq:
                    satisfies_clause = True
                    break
                    
            if satisfies_clause:
                result.add(molecule)
                print(f"Keeping molecule: {molecule.sequence} (satisfies literal {literal})")
            else:
                print(f"Removing molecule: {molecule.sequence} (satisfies no literals)")
        
        print(f"\nSatisfying molecules for clause {clause}:")
        for mol in result.molecules:
            print(f"  {mol.sequence}")
        
        return result

    
    def solve(self) -> bool:
        """Solve the 3-SAT problem using molecular operations."""
        current_tube = self._generate_initial_tube()
        print(f"\nInitial assignments: {len(current_tube.molecules)} molecules")
        
        for i, clause in enumerate(self.clauses):
            print(f"\nProcessing clause {i+1}: {clause}")
            current_tube = self._process_clause(current_tube, clause)
            print(f"After clause {i+1}: {len(current_tube.molecules)} molecules")
            
            if current_tube.is_empty():
                print("Formula is unsatisfiable")
                return False
        
        print("Formula is satisfiable")
        return True



def test_solver():
    """Test the molecular SAT solver with sample cases."""
    # Test satisfiable case
    print("\nTest 1 (should be satisfiable):")
    solver1 = MolecularThreeSATSolver(3)
    solver1.add_clause([1, 2, 3])
    solver1.add_clause([-1, 2, 3])
    result1 = solver1.solve()
    print(f"Result: {'satisfiable' if result1 else 'unsatisfiable'}")
    
    # Test unsatisfiable case
    print("\nTest 2 (should be unsatisfiable):")
    solver2 = MolecularThreeSATSolver(2)
    solver2.add_clause([1, 1, 2])
    solver2.add_clause([-1, -1, -2])
    solver2.add_clause([1, -2, -2])
    solver2.add_clause([-1, 2, 2])
    result2 = solver2.solve()
    print(f"Result: {'satisfiable' if result2 else 'unsatisfiable'}")

if __name__ == "__main__":
    test_solver()