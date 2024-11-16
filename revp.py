from Bio import SeqIO
from Bio.Seq import Seq 
def parse_fasta():
    for record in SeqIO.parse("rosalind_revp.txt", "fasta"): #rosalind dataset has to be present in the same folder as this file
        sequence=str(record.seq)
        return sequence
dna_data=parse_fasta()

def revp(dna_data):
    results=[]
    n=len(dna_data)
    for length in range(4,13):
        for i in range(n-length+1):
            substring=dna_data[i:i+length]
            sub_str=Seq(substring)
            if substring==str(sub_str.reverse_complement()):
                results.append((i+1,length))
    return results

result=revp(dna_data)
with open("revp.txt", "w") as f:
    for i in result:
        f.write(str(i[0])+" "+str(i[1])+"\n")

