#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_iev.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    

    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        months = [ int(i) for i in lines[0].strip().split(' ')]
       
        offspring = (1*months[0] + 1*months[1] + 1*months[2] + 0.75*months[3] + 0.5*months[4] + 0*months[5]) * 2
       
       
        print(offspring, file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)