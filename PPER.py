#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_pper.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


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
        
        lines = fin.readlines()
        n, k = [int(i) for i in lines[0].strip().split()]
        
        results = self.factorial(n) / self.factorial(n-k) 
        
        
        
        print (int(results% 1000000), file=fout)
        
       
    
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)