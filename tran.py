from Bio import SeqIO
def parse_fasta():
    dna_data=[]
    for record in SeqIO.parse("rosalind_tran.txt", "fasta"): #rosalind dataset has to be present in the same folder as this file
        sequence=str(record.seq)
        dna_data.append(sequence)
    return dna_data
dna_data=parse_fasta()

def tran(dna_data):
    str1=dna_data[0]
    str2=dna_data[1]
    transition_idx=0
    transversion_idx=0
    purines=['A','G']
    pyrimidines=['C','T']
    for i in range(len(str1)):
        n1=str1[i]
        n2=str2[i]
        if n1==n2:
            continue
        elif (n1 in purines and n2 in purines) or (n1 in pyrimidines and n2 in pyrimidines):
            transition_idx+=1
        elif (n1 in purines and n2 in pyrimidines) or (n1 in pyrimidines and n2 in purines):
            transversion_idx+=1
    tt_ratio=transition_idx/transversion_idx
    return tt_ratio

result=tran(dna_data)
print(result)
