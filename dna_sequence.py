class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.complementary_strand = self._generate_complementary_strand(sequence)
        self.is_valid_sequence()
    
    def is_valid_sequence(self):
        valid_nucleotides = set('ACGT')
        if not all(nucleotide in valid_nucleotides for nucleotide in self.sequence):
            raise ValueError("Invalid DNA sequence. Only A, C, G, T allowed.")
    
    @staticmethod
    def _generate_complementary_strand(sequence: str) -> str:
        """Generate the complementary DNA strand."""
        complement_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement_pairs[base] for base in sequence)


    
    def __str__(self):
        return f"5'-{self.sequence}-3'\n3'-{self.complementary_strand}-5'"

    def Sequence(self):
        """Return the DNA sequence."""
        return self.sequence

    def isDnaSequense(strand1, strand2):
        """
        Checks if two DNA strands are complementary.
        this method returns true if strand2 is the complementary strand of strand1.
        """
        complement_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        if len(strand1) != len(strand2):
            return False
        for b1, b2 in zip(strand1, strand2):
            if complement_pairs.get(b1) != b2:
                return False
        
        return True



    def cleave(self, enzymeRecognitionSeq):
        """
        Cut the DNA sequence at the recognition site of the enzyme.
        This function splits the sequence at every instance of the enzyme's recognition site.
        The enzyme is assumed to recognize a specific sequence and cut between the bases.
        
        Parameters:
        enzymeRecognitionSeq (str): The recognition site of the enzyme (the sequence to look for).
        
        Returns:
        List[str]: A list of DNA segments resulting from the cuts.
        """
        segments = []
        sequence = self.sequence
        enzyme_length = len(enzymeRecognitionSeq)
        
        # Split the sequence by the enzyme's recognition site
        parts = sequence.split(enzymeRecognitionSeq)
        
        # Add the first part (before the first cut) to the segments
        if parts[0]:
            segments.append(parts[0])
        
        # For each subsequent part, add only the part before the recognition site (no need to add enzyme again)
        for part in parts[1:]:
            if part:
                segments.append(part)
        
        # Return the segments formed after cleaving
        return segments



if __name__ == "__main__":
    sequence = "ATCGGAATTCGGAATTC"
    enzyme = "GAATTC" # EcoR1
    dna = DNASequence(sequence)
    result = dna.cleave(enzyme)
    print(result)  # output: ['ATCG', 'G']
