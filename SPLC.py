#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_splc.txt'
outFile = f"dataset/{os.path.basename(inFile)}.out"

def read_fasta(inFile):
    
    fin = open(inFile, 'r')
    seqs = {}
    seq = ''
    seqId = ''
    begin = True
    for l in fin.readlines():
        l = l.strip()
        if len(l) == 0: continue
        
        if l.startswith(">"):
            if not begin:
                seqs[seqId] = seq
            seq = ''
            seqId = l.lstrip(">")
            begin = False
        else:
            seq += l
    seqs[seqId] = seq
    fin.close()
    return seqs


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
        UAA *      CAA Q      AAA K      GAA E
        UAG *      CAG Q      AAG K      GAG E
        UGU C      CGU R      AGU S      GGU G
        UGC C      CGC R      AGC S      GGC G
        UGA *      CGA R      AGA R      GGA G
        UGG W      CGG R      AGG R      GGG G
        """
        for l in text.split("\n"):
            l = l.strip(' ')
            b = [ i.split(' ') for i in l.split('      ')]
            if len(b) <2: continue
           
            for k, v in b:
                table[k] = v
        return table
    
    def translate(self, seq):
        protein = ''
        codons = self.codon_table()
        for i in range(0, len(seq)-2, 3):
            if (codons[seq[i:i+3]] == "*"):
                break
            protein += codons[seq[i:i+3]]
        return protein
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        fasta = read_fasta(inFile)
        seq = list(fasta.values())[0]
        introns = list(fasta.values())[1:]
        
        spliceSeq = seq
        for intron in introns:
            spliceSeq = spliceSeq.replace(intron, '')
        
        spliceSeq = spliceSeq.replace('T', 'U')
        aa = self.translate(spliceSeq)
        print(aa, file=fout)
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)