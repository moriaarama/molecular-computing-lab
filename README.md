# 🧬 Molecular Computing Lab - DNA-Based Computational Simulation

A virtual molecular computing laboratory that demonstrates how DNA sequences can be used as computational data structures to solve complex problems. This project simulates various wet lab molecular biology processes and implements a molecular algorithm for solving the 3-SAT problem.

## 🔬 Project Overview

This repository demonstrates a virtual "molecular computing" lab that uses DNA strands as the primary data structure, modeling various real-world molecular biology processes including:

- **PCR Amplification** - Exponential DNA replication
- **Restriction Enzyme Digestion** - Sequence-specific DNA cutting
- **DNA Synthesis** - Custom sequence generation
- **Molecular Separation** - Target sequence extraction
- **Hybridization** - Complementary strand binding
- **Computational Problem Solving** - Using DNA for NP-complete problems (3-SAT)

The project culminates in a molecular computing approach to solve the 3-SAT Boolean satisfiability problem, demonstrating how biological processes can be harnessed for computational purposes.

## 📁 Project Structure

```
molecular-computing-lab/
├── dna_sequence.py      # Core DNA sequence class with molecular operations
├── PCRSimulator.py      # PCR amplification simulation
├── molecular_tube.py    # Container for DNA molecules with separation operations
├── solution.py          # 3-SAT solver using molecular computing approach
└── README.md           # This file
```

## 🧪 Core Components

### 1. DNASequence Class (`dna_sequence.py`)

The foundation class representing double-stranded DNA molecules with various molecular biology operations.

**Key Features:**
- **Sequence Validation**: Ensures only valid nucleotides (A, T, G, C)
- **Automatic Complementary Strand Generation**: Models Watson-Crick base pairing
- **Restriction Enzyme Simulation**: Sequence-specific cutting operations

**Main Functions:**

| Function | Purpose | Molecular Process Modeled |
|----------|---------|--------------------------|
| `__init__(sequence)` | Creates DNA molecule with complementary strand | DNA synthesis and hybridization |
| `is_valid_sequence()` | Validates nucleotide composition | Quality control in DNA synthesis |
| `_generate_complementary_strand()` | Creates Watson-Crick complement | DNA hybridization (A↔T, G↔C) |
| `cleave(enzymeRecognitionSeq)` | Cuts DNA at specific sequences | Restriction enzyme digestion |
| `isDnaSequense(strand1, strand2)` | Checks strand complementarity | Hybridization assay |

**Example Usage:**
```python
# Create DNA molecule
dna = DNASequence("ATCGGAATTCGGAATTC")

# Simulate EcoRI restriction digestion
fragments = dna.cleave("GAATTC")  # EcoRI recognition site
print(fragments)  # ['ATCG', 'G']
```

### 2. PCRSimulator Class (`PCRSimulator.py`)

Simulates Polymerase Chain Reaction (PCR) for exponential DNA amplification with error modeling.

**Molecular Process Modeled:** 
- DNA denaturation (strand separation)
- Primer annealing
- DNA polymerase extension
- Replication errors

**Key Functions:**

| Function | Purpose | Real PCR Step |
|----------|---------|---------------|
| `pcr_amplify(dna_sequence, num_cycles, error_rate)` | Exponential amplification | Complete PCR cycling |
| `get_complementary_base(base)` | Base pairing during synthesis | DNA polymerase activity |

**Features:**
- **Exponential Amplification**: 2^n molecules after n cycles
- **Error Modeling**: Simulates polymerase errors during synthesis
- **Cycle Tracking**: Models multiple PCR rounds

### 3. MolecularTube Class (`molecular_tube.py`)

Represents a test tube containing multiple DNA molecules, enabling molecular separation and analysis operations.

**Molecular Processes Modeled:**
- Gel electrophoresis separation
- Affinity purification
- Molecular filtering

**Key Functions:**

| Function | Purpose | Lab Technique Modeled |
|----------|---------|---------------------|
| `add(molecule)` | Add DNA to tube | Sample preparation |
| `extract(target_sequence)` | Isolate specific sequences | Affinity chromatography |
| `intersect(other_tube)` | Find common molecules | Comparative analysis |
| `is_empty()` | Check for molecules | Detection assay |

### 4. MolecularThreeSATSolver Class (`solution.py`)

Implements a molecular computing algorithm to solve the 3-SAT Boolean satisfiability problem using DNA operations.

**Computational Approach:**
- **DNA Encoding**: Each variable assignment encoded as DNA sequence
- **Parallel Processing**: All possible assignments generated simultaneously
- **Molecular Filtering**: Unsatisfying assignments removed by "molecular operations"

**Key Functions:**

| Function | Purpose | Molecular Operation |
|----------|---------|-------------------|
| `_initialize_encodings()` | Create unique DNA codes for variables | DNA synthesis |
| `_generate_initial_tube()` | Create all possible assignments | Combinatorial DNA library |
| `_process_clause()` | Filter assignments by clause satisfaction | Selective hybridization |
| `solve()` | Complete 3-SAT solving pipeline | Sequential molecular operations |

**Algorithm Steps:**
1. **Library Generation**: Create DNA molecules for all 2^n variable assignments
2. **Clause Processing**: For each clause, keep only molecules representing satisfying assignments
3. **Solution Detection**: Check if any molecules remain (satisfiable) or tube is empty (unsatisfiable)

## 🚀 Running the Lab

### Basic DNA Operations
```python
# Create and analyze DNA
from dna_sequence import DNASequence

dna = DNASequence("ATCGGAATTC")
print(dna)  # Shows double-stranded DNA
fragments = dna.cleave("GAATTC")  # Restriction digestion
```

### PCR Simulation
```python
from PCRSimulator import PCRSimulator

pcr = PCRSimulator()
amplified = pcr.pcr_amplify(dna, num_cycles=3, error_rate=0.001)
print(f"Amplified to {len(amplified)} molecules")
```

### Molecular Computing example:
```python
from solution import MolecularThreeSATSolver

# Solve 3-SAT problem: (x1 ∨ x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ x3)
solver = MolecularThreeSATSolver(3)
solver.add_clause([1, 2, 3])      # (x1 ∨ x2 ∨ x3)
solver.add_clause([-1, 2, 3])     # (¬x1 ∨ x2 ∨ x3)
is_satisfiable = solver.solve()
```

## 🧬 Molecular Computing Concepts

### DNA as Data Storage
- **4-bit encoding**: A, T, G, C represent different states
- **Complementarity**: Built-in error checking through base pairing
- **Massive parallelism**: Billions of molecules process simultaneously

### Biological Operations as Computation
- **Restriction enzymes**: Act as programmable "search and cut" operations
- **PCR amplification**: Provides exponential copying for signal amplification
- **Hybridization**: Enables sequence-specific molecular recognition
- **Separation techniques**: Allow filtering and sorting of molecular solutions

### Advantages of Molecular Computing
- **Massive Parallelism**: 10^18+ operations simultaneously
- **Energy Efficiency**: Biological processes are naturally optimized
- **Self-Assembly**: Molecules naturally organize through physical interactions
- **Miniaturization**: Molecular-scale components

## 📚 Scientific Background

This project is inspired by Leonard Adleman's pioneering 1994 experiment that solved the Hamiltonian Path Problem using DNA, launching the field of molecular computing. The 3-SAT solver implementation demonstrates how NP-complete problems can be approached using:

1. **Generate-and-Test Paradigm**: Create all possible solutions, then filter
2. **Molecular Parallelism**: Process all candidates simultaneously
3. **Biological Specificity**: Use molecular recognition for precise operations

## 🔬 Educational Applications

This virtual lab helps understand:
- **Molecular Biology Techniques**: PCR, restriction digestion, hybridization
- **Computational Complexity**: NP-complete problems and solution strategies
- **Biotechnology Applications**: How biology can solve computational problems
- **Algorithm Design**: Translating computational problems to molecular operations

## 🚧 Future Extensions

Potential enhancements for the virtual lab:
- **Gel Electrophoresis Simulation**: Visualize DNA separation by size
- **DNA Sequencing**: Implement Sanger or next-generation sequencing
- **Protein Synthesis**: Model translation from DNA to proteins
- **Additional NP Problems**: Hamiltonian Path, Graph Coloring, etc.
- **Error Analysis**: More sophisticated error models for PCR and sequencing

## 📖 References

- Adleman, L. M. (1994). "Molecular computation of solutions to combinatorial problems"
- Păun, G., Rozenberg, G., & Salomaa, A. (1998). "DNA Computing: New Computing Paradigms"
- Molecular Biology Laboratory Techniques and Standard Protocols

---

**Note**: This is a computational simulation for educational purposes. Real molecular computing experiments require specialized laboratory equipment and expertise in molecular biology techniques.