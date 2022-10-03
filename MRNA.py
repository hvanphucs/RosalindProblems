#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_mrna.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:
    
    def codon_table (self):
        table = {}
        text = """
        UUU F      CUU L      AUU I      GUU V
        UUC F      CUC L      AUC I      GUC V
        UUA L      CUA L      AUA I      GUA V
        UUG L      CUG L      AUG M      GUG V
        UCU S      CCU P      ACU T      GCU A
        UCC S      CCC P      ACC T      GCC A
        UCA S      CCA P      ACA T      GCA A
        UCG S      CCG P      ACG T      GCG A
        UAU Y      CAU H      AAU N      GAU D
        UAC Y      CAC H      AAC N      GAC D
        UAA Stop      CAA Q      AAA K      GAA E
        UAG Stop      CAG Q      AAG K      GAG E
        UGU C      CGU R      AGU S      GGU G
        UGC C      CGC R      AGC S      GGC G
        UGA Stop      CGA R      AGA R      GGA G
        UGG W      CGG R      AGG R      GGG G
        """
        for l in text.split("\n"):
            l = l.strip(' ')
            b = [ i.split(' ') for i in l.split('      ')]
            if len(b) <2: continue
           
            for k, v in b:
                table[k] = v
        return table
    
    def codon(self):
        dit = {}
        for k, v in self.codon_table().items():
            if v in dit:
                dit[v].append(k)
            else:
                dit[v] = [k]
        return dit
    
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        aaSeq = lines[0].strip()
        ditCodon = self.codon()
        
        num = 1
        for aa in aaSeq:
            num *= len(ditCodon[aa])
        num = num *len(ditCodon['Stop'])
        
        print(num% 1000000, file = fout)
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)