#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_fib.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"




class Solution:
    
    def fib(self, n,k):
        if (n<2): return 1
        
        return self.fib(n-1, k) + k *self.fib(n-2, k)
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        n, k = [int(i) for i in lines[0].split(' ')]
        print(self.fib(n, k), file=fout)
       
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)