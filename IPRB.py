#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_iprb.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        k, m, n = [int(i) for i in lines[0].split(' ')]
        
        a = k + m + n
        
        p1 = (1/4*m*(m-1) + 1/2*m*n + 1/2*m*n + n*(n-1))/(a*(a-1))
       
      
    
        print(1-p1, file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)