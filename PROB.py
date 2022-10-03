#!/usr/bin/env python3

import os, sys
import math


'''


'''

inFile = 'dataset/rosalind_prob.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        seq = lines[0].strip()
        A = [float(i) for i in lines[1].strip().split(' ')]
        
        a = seq.count('A') + seq.count('T')
        c = seq.count('C') + seq.count('G')
        
        
        results = []
        for i in A:
            p = a *math.log((1-i)/2, 10) + c*math.log(i/2, 10)
            results.append(str(p))

        print(" ".join(results), file= fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)