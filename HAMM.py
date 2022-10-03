#!/usr/bin/env python3
from dis import dis
import os, sys

import os, sys

'''
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
'''

inFile = 'dataset/rosalind_hamm.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        seq1 = lines[0].strip()
        seq2 = lines[1].strip()
        assert len(seq1) == len(seq2)
        
        diff = [1 for i in range(len(seq1)) if seq1[i] != seq2[i]]
        distance = sum(diff)
       
        print(distance, file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)