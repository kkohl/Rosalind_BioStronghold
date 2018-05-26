# Rosalind
# Bioinformatics Stronghold
# ID: REVC


# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

s = "GGTGCAATTGTCGCGGATGGCCGTTTCGCCCCGTAGTCGTCCTGGCCCGCCAAAAAGTGTCCACCATGGTAGACACGGTGCGGGGGGTTTAATTAATGAACTGATAAGTTACGTGCACCCCAGTGTTCAAGAGAGTCCGAAAGGTATGCTAAGCGTTGTTCTGAGCGGAATATCAACTAAAGACAGTGCTTACACTTCAAGCTCTTAAATAACCAGCATTATCAGTGAACCATTGTGTGCCCTATCTATCTCGTAACTTACTTTGCACTCCCCTCGAGGGTCCGACAGATCATTAGATATGCTAGTGATGATCGTACATTTGGCCTAGTCAAGTATGGGATCACAGTACAACTCCGGGCGTCTAGAACCGAGTAAGACGGCCCAAAAATTGCGGGTTTTTGTGACCTATTCCACGCTTTCGTTAAGGAAGGTACGAAGAAAAACGATAAAAAGCCTTCAGCTTGCTGCTAGTGGGTAAACGTGATTTTCGGTCATCCCACGGATCTTTAAAGCTGCAACCATGAGGTGCAGCCACATGAGACGTCAGTTTAAGAGTTGTAAGTCGCACCACTGCGCACTTGAGGTAGCTATTATTCCCCGCTCCTTGTTTAAGTCGACCGTAATCAAAAAATATCATCTGTCGGCCCCGTAAACTGTCGTACTACTTCTTTGAATGGCTTTAGAGCAGGTCCGTTGGCACTATAGATGAAAATCGTGTCTGGAGAACGAACTCCCGTCTGACACCCGATCTGGTCATTAGGGGGAGGATTTCCTAACGCTACTGACGTTGTTTTGCCGGGTCGGTTCGGTTATGCCCGACGTGTCAGTGATCATGAGCAAACTCAACCCAGCTTCGCCCCAAATCGGTGCGGGCCAGGCGGGCGGAGGGTGGTGTCCTGTTAATTTCCAGATTATCTAAGATCGAGACGGTTATCTCCGTAATTAGTGTGGCCCGTCGGGACCTGGAGAAGTTACATAGAAAATTTACTAACC"


def complement(dna):
    
    # create empty string
    sc = ""
    
    # create refrence dictionary for complements
    comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
	
	# loop through strand and replace with complement
    for base in dna.upper():
		# add new nt at beginning to reverse
        sc = comp[base] + sc

    return sc


print(complement(s))
