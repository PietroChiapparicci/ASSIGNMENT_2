aa_n_codons={
    'A': 4,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 4,
    'H': 2,
    'I': 3,
    'K': 2,
    'L': 6,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 2,
    'R': 6,
    'S': 6,
    'T': 4,
    'V': 4,
    'W': 1,
    'Y': 2 
    }

def mrna(P):
    n_ways=1
    mod=1000000
    for i in P:
        n_ways*=aa_n_codons[i]
    n_ways*=3 #there are three codons that encode for a stop codon
    n_ways=n_ways%mod
    return n_ways

P=''
result=mrna(P)
print(result)