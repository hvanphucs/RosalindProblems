#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_pmch.txt'
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
    
    def factorial(self, n):
        f = 1
        for i in range(n):
            f  *= (i+1)
        return f
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        fasta = read_fasta(inFile)
        seq = list(fasta.values())[0]
        
        a = seq.count('A')
        c = seq.count('C')
        
        print (a, c)
        
        results = self.factorial(a) * self.factorial(c)
        
        #results = long(results% 1000000)
        #print (str(results))
        print (str(results), file=fout)
        
       
    
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)