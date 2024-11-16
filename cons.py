from Bio import SeqIO

def parse_fasta():
    dna_data=[]
    for record in SeqIO.parse("rosalind_cons.txt", "fasta"): #rosalind dataset has to be present in the same folder as this file
        sequence=str(record.seq)
        dna_data.append(sequence)
    return dna_data
dna_data=parse_fasta()

def cons(dna_data):
    consensus=[]
    seq_lenght=len(dna_data[0])
    for i in range(seq_lenght):
        idxA=0
        idxG=0
        idxT=0
        idxC=0
        for seq in dna_data:
            if seq[i]=='A':
                idxA+=1
            elif seq[i]=='C':
                idxC+=1
            elif seq[i]=='G':
                idxG+=1
            elif seq[i]=='T':
                idxT+=1
        max_count=max(idxA,idxC,idxG,idxT)
        
        if max_count==idxA:
            consensus.append('A')
        elif max_count==idxC:
            consensus.append('C')
        elif max_count==idxG:
            consensus.append('G')
        else:
            consensus.append('T')
    return ''.join(consensus)


def profile_matrix(dna_data):
    seq_length=len(dna_data[0])
    profile_matrix={'A':[0]*seq_length,'C':[0]*seq_length,'G':[0]*seq_length,'T':[0]*seq_length}
    for seq in dna_data:
        for i in range(seq_length):
            nucleotide=seq[i]
            profile_matrix[nucleotide][i]+=1
    return profile_matrix


result=cons(dna_data)
matrix=profile_matrix(dna_data)
with open("cons.txt", "w") as f:
    f.write(result+"\n")
    for nucleotide in ['A', 'C', 'G', 'T']:
        f.write(f"{nucleotide}: {' '.join(map(str, matrix[nucleotide]))}\n")
