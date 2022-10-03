#!/usr/bin/env python3

import os, sys
import itertools


'''


'''

inFile = 'dataset/rosalind_kmer.txt'
#inFile = 'dataset/problem.in'
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
        
        kmers = ["".join( i)  for i in itertools.product('ATGC', repeat=4)]
        
        
        dit = { kmer: 0 for kmer in kmers}
        dit = dict(sorted(dit.items()))
        
        
        for i in range(len(seq)-4+1):
            kmer = seq[i: i+4]
            if len(kmer) != 4: continue
            dit[kmer]+=1
       
       
        print (dit)
        for i in sorted(kmers):
            print (dit[i], end=' ', file=fout)
       
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)