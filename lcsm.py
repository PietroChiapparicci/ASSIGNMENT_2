from Bio import SeqIO
def parse_fasta():
    dna_data=[]
    for record in SeqIO.parse("rosalind_lcsm.txt", "fasta"): #rosalind dataset has to be present in the same folder as this file
        sequence=str(record.seq)
        dna_data.append(sequence)
    return dna_data
dna_data=parse_fasta()

def lcsm(dna_data):
    shortest_str=dna_data[0]
    for dna in dna_data:
        if len(dna)<len(shortest_str):
            shortest_str=dna
    length=len(shortest_str)
    for i in range(length,0,-1):
        for sp in range(length-i+1):
            common_str=shortest_str[sp:sp+i]
            str_in_common=True
            for dna in dna_data:
                if common_str not in dna:
                    str_in_common=False
                    break
            if str_in_common==True:
                return common_str
            
result=lcsm(dna_data)
print(result)