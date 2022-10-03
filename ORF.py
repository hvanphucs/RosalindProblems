#!/usr/bin/env python3

import os, sys



'''


'''

inFile = 'dataset/rosalind_orf.txt'
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
    
    def toProtein(self, seq, frame = 1):
        codons = self.codon_table()
        dit = {
            "A": "U", "T" : "A",
            "G": "C", "C": "G",
            "U": "A",
            }
        #transcript =  "".join([dit[nu] for nu in seq])
        transcript = seq.replace('T', 'U')
        transcript = transcript[frame-1:]
        aa = ''
        for i in range(0, len(transcript)-2, 3):
            aa += codons[transcript[i:i+3]]
        return aa
        
    def reverseComplement(self, seq):
        seq = seq[::-1]
        dit = {
            "A": "T", "T": "A",
            "G": "C", "C": "G"
        }
        return "".join([dit[nu] for nu in seq])


    
    def toFrame(self, seq):
       
        results = []
        aaSeq1 = self.toProtein(seq, frame=1)
        aaSeq2 = self.toProtein(seq, frame=2)
        aaSeq3 = self.toProtein(seq, frame=3)
        print(aaSeq1.replace("M", ">"))
        print(aaSeq2.replace("M", ">"))
        print(aaSeq3.replace("M", ">"))
        
        
        for aaSeq in [aaSeq1, aaSeq2, aaSeq3]:
           
            for i in range(len(aaSeq)):
                if (aaSeq[i] == 'M' and aaSeq.find('*', i) != -1):
                    results.append(aaSeq[i: aaSeq.find('*', i)])
        return results
    
    def res (self, inFile, outFile):
        print ('Run solution for dataset: %s' % inFile)
        fin  = open(inFile, 'r')
        fout = open(outFile, 'w')
        
        fasta = read_fasta(inFile)
        seq = list(fasta.values())[0]
        rcpSeq = self.reverseComplement(seq)
        
        
       
        
        framePlus = self.toFrame(seq)
        frameMinus = self.toFrame(rcpSeq)
        allProtein = set(framePlus + frameMinus)
        
        for aa in allProtein:
            print(aa, file = fout)
        
        fin.close()
        fout.close()
        pass


Solution().res(inFile, outFile)