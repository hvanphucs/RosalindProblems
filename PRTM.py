#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_prtm.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    def massTable(self):
        
        text = f"""
            A   71.03711
            C   103.00919
            D   115.02694
            E   129.04259
            F   147.06841
            G   57.02146
            H   137.05891
            I   113.08406
            K   128.09496
            L   113.08406
            M   131.04049
            N   114.04293
            P   97.05276
            Q   128.05858
            R   156.10111
            S   87.03203
            T   101.04768
            V   99.06841
            W   186.07931
            Y   163.06333 
        """
        
        dit = {}
        
        for l in text.split("\n"):
            l = l.strip().split('   ')
            if len(l) != 2: continue
            dit[l[0]] = float(l[1])
        return dit
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        aa = lines[0].strip()
        massTable = self.massTable()
        
        mass = [massTable[i] for i in aa]
        
       
       
    
        print(sum(mass), file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)