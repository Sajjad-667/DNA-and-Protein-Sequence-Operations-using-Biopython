# ***** Reverse Complement of a DNA Sequence *****

from Bio.Seq import Seq  # Import the Seq class from Biopython

# Define a DNA sequence
dna = Seq("ATGCGTAC")

# Print the original and reverse complement DNA sequences
print("Original DNA Sequence:     ", dna)
print("Reverse Complement:        ", dna.reverse_complement())


# ***** Transcribe DNA to RNA *****

from Bio.Seq import Seq  # Redundant but kept for clarity if code blocks are run independently

# Define a DNA sequence
dna = Seq("ATGGCCAATTG")

# Transcribe the DNA to RNA
rna = dna.transcribe()

# Print the RNA sequence
print("RNA Sequence:              ", rna)


# ***** Translate DNA to Protein *****

from Bio.Seq import Seq  # Again, re-importing for modularity

# Define a DNA sequence
dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Translate the DNA to a protein sequence
protein = dna.translate()

# Print the protein sequence
print("Protein Sequence:          ", protein)


# ***** Find Molecular Weight of a Protein Sequence *****

from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight  # Import function to compute molecular weight

# Define a protein sequence
protein_seq = Seq("MVKVYAPASSANMSVGFDVLGAAVTPVDGALLGDVVTVEAAETFSLNNLGQK")

# Calculate the molecular weight of the protein
mw = molecular_weight(protein_seq, seq_type='protein')

# Print the molecular weight
print(f"Molecular Weight of Protein: {mw:.2f} Da")