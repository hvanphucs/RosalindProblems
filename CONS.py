#!/usr/bin/env python3
import os, sys

'''

'''

inFile = 'dataset/rosalind_cons.txt'
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
    
    def getMaxItem(self, dit):
        maxItem = list(dit.items())[0]
        for k, v in dit.items():
            if v > maxItem[1]:
                maxItem = [k,v]
        return maxItem
            
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        
        
        seqs = read_fasta(inFile)
        seqStrings = list(seqs.values())
        
        lenSeq = len(seqStrings[0])
        
        matrix = []
        for i in range (lenSeq):
            matrix_nu = { nu : 0 for nu in list('ACGT')}
            for seqString in seqStrings:
               matrix_nu[seqString[i]] +=1
            matrix.append(matrix_nu)
        
        consenus = "".join([ self.getMaxItem(i)[0] for i in matrix])
        print(consenus, file= fout)
        
        
        for nu in 'ACGT':
            freq = ' '.join([str(i[nu]) for i in matrix ])
            print(f"{nu}: {freq}", file= fout)
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)