#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_sseq.txt'
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
    
    def findMotif(self,seq, motif):
        pos = [0]
        
        for i in motif:
            #print (i)
            nextIndex = seq[ pos[-1]:].index(i)
            newPos = nextIndex + 1 + pos[-1]
           
            pos.append(newPos)
            
        return [ str(i) for i in pos[1:]]
            
            
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        fasta = read_fasta(inFile)
        seq = list(fasta.values())[0]
        motif = list(fasta.values())[1]
        
       
        results = self.findMotif(seq, motif)
        
        print (seq, motif, results)
       
        print(' '.join(results), file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)