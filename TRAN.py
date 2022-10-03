#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_tran.txt'
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
        seq1 = list(fasta.values())[0]
        seq2 = list(fasta.values())[1]
        
        transition = 0
        transversion = 0
        
        for i in range(len(seq1)):
            pair = sorted([seq1[i], seq2[i]])
            pair = "".join(pair)
            
            if pair in ['AG', 'GA', 'TC', 'CT']:
                transition +=1
            elif pair not in ['AA', 'TT', 'GG', 'CC']:
                transversion +=1
       
        
    
        print(transition/transversion, file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)