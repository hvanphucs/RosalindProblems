#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_tree.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        n = int(lines[0].strip())
        adjacencyList = [ i.strip(' ').split(' ') for i in lines[1:]]
        
        subtrees = []
        nodes = set()
        
        for i, j in adjacencyList:
            if i in nodes or j in nodes:
                for subtree in subtrees:
                    if i in subtree or j in subtree:
                        indexTree = subtrees.index(subtree)
                        subtrees[indexTree].append(i)
                        subtrees[indexTree].append(j)
                        nodes.add(i)
                        nodes.add(j)
            else:
                subtrees.append([i, j])
                nodes.add(i)
                nodes.add(j)
                
        l = len(subtrees)
        for i in range(l):
            for j in range(l):
                if (i==j): break
                if len(set(subtrees[i] + subtrees[j])) < len(subtrees[i]) + len(subtrees[j]):
                    subtrees[i] = list(set(subtrees[i] + subtrees[j]))
                    subtrees[j] = []
        subtrees = [i for i in subtrees if i]  
        
        results = (n - len(nodes)) + len(subtrees) #-1    
        
        print (results, file =fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)