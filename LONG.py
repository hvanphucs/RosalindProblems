#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_long.txt'
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
    
    def findOverlap(self, seq1, seq2):
        combineStrings = []
        overlapStrings = []
        for i in range(len(seq1)):
            if seq1[i:] == seq2[:len(seq1)-i]:
                overlapStrings.append(seq1[i:])
                combineStrings.append(seq1+seq2[len(seq1)-i:])
                break
        for i in range(len(seq2)):
            if seq2[i:] == seq1[:len(seq2)-i]:
                overlapStrings.append(seq2[i:])
                combineStrings.append(seq2+seq1[len(seq2)-i:])
                break
        if not overlapStrings:
            return "", ""

        combineStrings = min(combineStrings, key=len)
        overlapStrings = max(overlapStrings, key=len)
        return combineStrings, overlapStrings
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        fasta = read_fasta(inFile)

        tmp = list(fasta.values())
        
        while (len(tmp) >1):
            bestOverlapString = ''
            bestOverlapStringPair = [ '', '']
            bestOverlapStringLength = 0
            
            for i in range(len(tmp)-1):
                for j in range(i+1, len(tmp)):
                    
                    combineString, overlapString = self.findOverlap(tmp[i], tmp[j])
                    print('Find overlap: ', i, j, combineString)
                    if len(overlapString) > bestOverlapStringLength:
                        bestOverlapString = combineString
                        bestOverlapStringPair = [tmp[i], tmp[j]]
                        bestOverlapStringLength = len(overlapString)
            for i in bestOverlapStringPair:
                if i in tmp: 
                    tmp.remove(i)
                
               
            tmp.append(bestOverlapString)
        print (tmp[0], file = fout)    
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)