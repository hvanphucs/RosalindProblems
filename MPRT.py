#!/usr/bin/env python3

import os, sys
import urllib.request
import re


'''


'''

inFile = 'dataset/rosalind_mprt.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"


class Solution:

    def getUniProt(self,ids):
        seqs = {}
        for id in ids:
            try:
                requestId = id.split("_")[0]
                url = f"http://www.uniprot.org/uniprot/{requestId}.fasta"
                response = urllib.request.urlopen(url)
                data = response.readlines()
                # print(data)
                for line in data:
                    line = line.decode("utf-8")
                    if line.startswith(">"):
                        seqs[id] = ''
                    else:
                        seqs[id] += line.strip()
            except Exception as e:
                print (e)
                print (f'Error on: {id}')
        return seqs
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        lines = fin.readlines()
        ids = [i.strip() for i in lines]
        seqs = self.getUniProt( ids)
        for i in seqs.keys():
            motifLocation = []
            p = re.compile(r'N[^P](S|T)[^P]')
            for j in range(len(seqs[i]) -3):
                if p.match(seqs[i][j:j+4]):
                    motifLocation.append(str(j+1))
            
            motifLocation = " ".join(motifLocation)
            if (motifLocation != ''):
                print(f"{i}\n{motifLocation}", file=fout)
                    

        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)