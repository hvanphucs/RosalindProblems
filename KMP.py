#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_kmp.txt'
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
        
        fasta = read_fasta(inFile)
        
        seq = list(fasta.values())[0]
        
        pArray = [0]*len(seq)
        longest = 0
        for i in range(1, len(seq)):
            for j in range(1, len(seq)-i +1):
                if (seq[:i] == seq[j:j+i]):
                    pArray[i+j-1] = len(seq[:i])
                    longest =  len(seq[:i])
                
            if (longest < len(seq[:i])):
                break
        for i in pArray:
            print(i, end=' ', file=fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)