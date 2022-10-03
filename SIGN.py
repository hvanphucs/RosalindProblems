#!/usr/bin/env python3

import os, sys
import itertools


'''


'''

inFile = 'dataset/rosalind_sign.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        n = int(lines[0].strip())
        
        pool = [ i for i in range(-n, n+1) if i != 0]
        
        results = list(itertools.permutations(pool, n))
        filterResults = []

        for pair in results:
            list1 = [ abs(i) for i in pair]
            if len(set(list1)) != n:
                continue
            filterResults.append([str(i) for i in pair])
        
        print (len(filterResults), file=fout)
        for i in filterResults:
            print(" ".join(i), file=fout)
        
        
        print (filterResults)
        
        
       
       
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)