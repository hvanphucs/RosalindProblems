#!/usr/bin/env python3

from cmath import log
import os, sys



'''


'''

inFile = 'dataset/rosalind_lcsm.txt'
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
    
    def getUniqKmers(self, seq, k):
        uniqKmers = []       
        for i in range(len(seq)):
            kmer = seq[i: i+k]
            if len(kmer) < k: break
            if kmer in uniqKmers: continue
            uniqKmers.append(kmer)
        return uniqKmers
    
    # def countUniqKmers(self, seqs, k):
    #     numberSeq = len(seqs)
        
    #     countKmers = {}
        
    #     for seq in seqs:
    #         uniqKmersOnSeq = self.getUniqKmers(seq, k)
    #         for kmer in uniqKmersOnSeq:
    #             if kmer in countKmers:
    #                 countKmers[kmer] +=1
    #             else:
    #                 countKmers[kmer] = 1
    #             # check kmers frequency == numberSeq
    #             if (countKmers[kmer] == numberSeq):
    #                 return kmer
    #     return False
    
    
            
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        seqs = read_fasta(inFile)
        minSeq = min(seqs.items(), key=lambda k: len(k[1]))
        minLen = len(minSeq[1])
        
        longestKmer = False
        for length in range(minLen):
            longest = minLen - length
            uniqKmers = self.getUniqKmers(minSeq[1],longest )
            
          
            for uniqKmer in uniqKmers:
                share = True
                for seq in list(seqs.values()):
                    if uniqKmer not in seq:
                        share = False
                        break
                if  share:
                    longestKmer = uniqKmer
                    print(longestKmer, file=fout)
                    break
            if longestKmer:
                break
        
        if not longestKmer:
            print('Not found', file=fout)   
            
            
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)