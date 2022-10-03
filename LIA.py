#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_lia.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    def factorial(self, n):
        f = 1
        for i in range(1, n+1):
            f = f*i
        return f
    
    def combine(self, i, j):
        return self.factorial(i)/ (self.factorial(j) * self.factorial(i-j))
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        k, n  = [int(i) for i in lines[0].strip().split(' ')]
        
        p = 0
        c = pow(2, k)
        for i in range(n, c +1):
            p += self.combine(c, i) * pow(0.25, i) * pow(0.75, c -i)

        
      
        print(p, file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)