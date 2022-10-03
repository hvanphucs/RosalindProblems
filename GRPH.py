#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_grph.txt'
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
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        n = 3
        fasta = read_fasta(inFile)
        seqs = list(fasta.values())
        ids = list(fasta.keys())
        
        for i in range(len(seqs)):
            for j in range(len(seqs)):
              
                if (i != j) and (seqs[i][-n:] == seqs[j][:n]):
                    print(ids[i], ids[j], file = fout)
                  
        
                
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)