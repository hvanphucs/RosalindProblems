#!/usr/bin/env python3

import os, sys
import itertools


'''


'''

inFile = 'dataset/rosalind_lexf.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        symbols = lines[0].strip().split(' ')
        n = int(lines[1].strip())
        
        result = list(itertools.product(symbols, repeat=n))
        print(result)
        print('\n'.join(["".join(i) for i in result]), file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)