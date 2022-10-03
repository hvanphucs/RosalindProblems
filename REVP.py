#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_revp.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"

def read_fasta(inFile):
    
    fin = open(inFile, 'r')
    seqs = {}
    seq = ''
    seqId = ''
    begin = True
    for l in fin.readlines():
        l = l.strip()
        if len(l) == 0: continue
        
        if l.startswith(">"):
            if not begin:
                seqs[seqId] = seq
            seq = ''
            seqId = l.lstrip(">")
            begin = False
        else:
            seq += l
    seqs[seqId] = seq
    fin.close()
    return seqs

class Solution:
    
    def reverseComplement(self, seq):
        seq = seq[::-1]
        dit = {
            "A": "T", "T": "A",
            "G": "C", "C": "G"
        }
        return "".join([dit[nu] for nu in seq])
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        fasta = read_fasta(inFile)
        seq = list(fasta.values())[0]
        
        for i in range(len(seq)):
            for j in range(4, 13):
                seq1 = seq[i: i+j]
                seq2 = self.reverseComplement(seq1)
                if (seq1 == seq2 and i+j <= len(seq)):
                    print(i+1, j, file=fout)
       
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)