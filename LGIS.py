#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_lgis.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    def longestIncrease(self, n, nums):
        list1 = []
        list2 = []
        for i in range(n):
            list1.append(1)
            list2.append([nums[i]])
            
            for j in range(i):
                if (nums[j] < nums[i]):
                    list1[i] = max(list1[i], list1[j] +1)
                    if(len(list2[i]) <= len(list2[j])):
                        list2[i] = list2[j] + [nums[i]]
        maxIndex = list1.index(max(list1))
        
        return list2[maxIndex]
        
    def longestDecrease(self, n, nums):
        list1 = []
        list2 = []
        for i in range(n):
            list1.append(1)
            list2.append([nums[i]])
            
            for j in range(i):
                if (nums[j] > nums[i]):
                    list1[i] = max(list1[i], list1[j] +1)
                    if(len(list2[i]) <= len(list2[j])):
                        list2[i] = list2[j] + [nums[i]]
        maxIndex = list1.index(max(list1))
        return list2[maxIndex]
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        n = int(lines[0].strip())
        nums = [ int(i) for i in lines[1].strip().split()]
        
        res1 = self.longestIncrease(n, nums)
        res2 = self.longestDecrease(n, nums)
        
        print(' '.join([str(i) for i in res1]), file=fout)
        print(' '.join([str(i) for i in res2]), file=fout)
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)