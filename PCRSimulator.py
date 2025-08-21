from dna_sequence import DNASequence
class PCRSimulator:
    @staticmethod
    def get_complementary_base(base):
        complement_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return complement_pairs[base]

    def pcr_amplify(self, dna_sequence, num_cycles=1, error_rate=0.001):
        """
        Simulate PCR amplification process.
        
        Steps for every cycle:
        1. Separate double strands into single strands
        2. Annealing: Primers attach (implicit in this simulation)
        3. Extension: Build complementary strands
        4. Result: Double the number of DNA molecules
        
        params:
            dna_sequence: Initial DNASequence object
            num_cycles: number of PCR cycles
            error_rate: Probability of error during synthesis
        
        return:
            List of DNASequence objects after amplification
        """
        import random
        
        current_molecules = [dna_sequence] # Starting with one double-stranded DNA molecule
        
        for cycle in range(num_cycles):
            new_molecules = []
            
            for molecule in current_molecules:
                # Step 1:  Separate into single strands
                strand1 = molecule.sequence
                strand2 = molecule.complementary_strand
                
                # Step 2 & 3: For each single strand, synthesize its complement

                #  first strand
                new_strand1 = strand1
                new_complementary1 = ""
                for base in new_strand1:
                    if random.random() < error_rate:
                        # Introduce error
                        possible_bases = list({'A', 'T', 'G', 'C'} - {self.get_complementary_base(base)})
                        new_complementary1 += random.choice(possible_bases)
                    else:
                        new_complementary1 += self.get_complementary_base(base)
                
                #  second strand
                new_strand2 = strand2
                new_complementary2 = ""
                for base in new_strand2:
                    if random.random() < error_rate:
                        # Introduce error
                        possible_bases = list({'A', 'T', 'G', 'C'} - {self.get_complementary_base(base)})
                        new_complementary2 += random.choice(possible_bases)
                    else:
                        new_complementary2 += self.get_complementary_base(base)
                
                # Create two new double-stranded molecules
                new_molecules.append(DNASequence(new_strand1))
                new_molecules.append(DNASequence(new_strand2))
            
            current_molecules = new_molecules
        
        return current_molecules


def test_pcr():
    # Create initial DNA sequence
    initial_dna = DNASequence("AGCT")
    print("Initial DNA molecule:")
    print(initial_dna)
    print(f"Number of molecules: 1")
    
    # Run PCR for 3 cycles
    pcr = PCRSimulator()
    result = pcr.pcr_amplify(initial_dna, num_cycles=3)
    
    print("\nAfter PCR amplification (3 cycles):")
    print(f"Number of molecules: {len(result)}")
    print("\nExample molecules:")
    for i, molecule in enumerate(result[:2]):  # Show first two molecules
        print(f"\nMolecule {i+1}:")
        print(molecule)

if __name__ == "__main__":
    test_pcr()