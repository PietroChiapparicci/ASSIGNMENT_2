from Bio import SeqIO
def parse_fasta():
    dna_data=[]
    for record in SeqIO.parse("rosalind_splc.txt", "fasta"): #rosalind dataset has to be present in the same folder as this file
        sequence=str(record.seq)
        dna_data.append(sequence)
    return dna_data
dna_data=parse_fasta()

def splc(dna_data):
    dna_string=dna_data[0]
    splicing_seq=dna_data[1:]
    for i in splicing_seq:
        dna_string=dna_string.replace(i,'')
    return dna_string
dna_string=splc(dna_data)

def rna(dna_string):
    mrna=""
    for i in dna_string:
        if i=="T":
            mrna+="U"
        else:
            mrna+=i
    return mrna
mrna=rna(dna_string)

gen_code= {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S',
    'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
    'CCA': 'P', 'CCG': 'P', 'CCU': 'P', 'CCC': 'P',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'UAA': '', 'UAC': 'Y', 'UAG': '', 'UAU': 'Y', 
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
    'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
}
def prot(mrna):
    final_prot=""
    for i in range(0, len(mrna),3):
        final_prot+=gen_code[mrna[i:i+3]]
    return final_prot
final_prot=prot(mrna)
print(final_prot)