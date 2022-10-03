#!/usr/bin/env python3

import os, sys
import itertools


'''


'''

inFile = 'dataset/rosalind_perm.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    def permutation(self, n):
        
        list1 = []
        for i in range(n):
            list1.append(i + 1)
        list2 = list(itertools.permutations(list1, n))
        return list2
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        n = int(lines[0].strip())
        
        list2 = self.permutation(n)
        print(len(list2), file=fout)
        for lst in list2:
            print (" ".join([str(i) for i in lst]), file=fout)
        
       
        
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)