#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_fibd.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        n, m  = [int (i) for i in lines[0].split(' ')]
        
        num = [0, 1]
        
        for i in range(1, n+1):
            if i < m:
                num.append(num[i] + num[i-1])
            if i > m:
                num.append(num[i] + num[i-1] - num[i-m])
                
            if i == m:
                num.append(num[i] + num[i-1] - num[i-m +1])
            
            
       
       
        print(num[n], file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)