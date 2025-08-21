from dna_sequence import DNASequence
from typing import List, Set, Dict, Optional

class MolecularTube:
    """Represents a molecular tube containing DNA sequences."""
    def __init__(self, name: str):
        self.name = name
        self.molecules: Set[DNASequence] = set() #using a set- no duplications
    
    def add(self, molecule: DNASequence) -> None:
        """Add a molecule to the tube."""
        self.molecules.add(molecule)
    
    
    def is_empty(self) -> bool:
        """Check if the tube is empty."""
        return len(self.molecules) == 0
    
    def extract(self, target_sequence: str) -> 'MolecularTube':
        """Extract molecules containing the target sequence."""
        result = MolecularTube(f"extract_{target_sequence}")
        
        # Check each molecule for the target sequence at the correct position
        sequence_len = len(target_sequence)
        for molecule in self.molecules:
            # Check the sequence at every possible position divisible by 3
            for i in range(0, len(molecule.sequence) - sequence_len + 1, 3):
                if molecule.sequence[i:i+sequence_len] == target_sequence:
                    result.add(molecule)
                    break
        return result

    def __str__(self) -> str:
        molecules_str = "\n".join(str(m) for m in self.molecules)
        return f"Tube {self.name}: {len(self.molecules)} molecules\n{molecules_str}"


    def intersect(self, other: 'MolecularTube') -> 'MolecularTube':
        """Return a new tube with molecules present in both tubes."""
        result = MolecularTube(f"intersect_{self.name}_{other.name}")
        result.molecules = self.molecules.intersection(other.molecules)
        return result