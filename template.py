#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/problem.in'
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
        
        lines = fin.readlines()
        sString = lines[0].strip()
        tString = lines[1].strip()
        
       
        locations = []
        
        for i in range(0, len(sString)):
            subString = sString[i:i+len(tString)]
            
            if (subString == tString):
                locations.append(str(i+1)) # using 1-based numbering, 
    
        print(' '.join(locations), file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)