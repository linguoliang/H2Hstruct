# coding=utf-8
import optparse
import sys
import time
from math import floor

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-19'
global h2hbase
h2hbase=0
biglist=[]
class H2H_gene_structs:
    '''
    这个类是用来存储H2H gene 的信息
    #pairID 0	species 1	Tax_id 2	PosSymbol_NegSymbol 3	chromosome 4	PosSymbol 5	PosGeneID 6	PosStart 7
    PosStop 8	NegSymbol 9	NegGeneID 10	NegStart 11	NegStop 12	TssDist 13	DistClass 14	BlockLength 15
    BlockStart 16	BlockStop 17	PosSynonyms 18	NegSynonyms 19
    '''
    def __init__(self,listinf):
        self.inf=listinf

    def isoverlab(self):
        if int(self.inf[7])>int(self.inf[12]):
            return False
        else:
            return True
    def getcenter(self):
        return str(floor((int(self.inf[7])+int(self.inf[12]))/2))

    def getposstart(self):
        return self.inf[7]

    def getnegstart(self):
        return self.inf[12]

    def returnbedformate(self):
        bedform=self.inf[4]+'\t'+self.inf[16]+'\t'+self.inf[17]+'\t'+self.inf[3]
        return bedform

    def getposend(self):
        return self.inf[8]

def readh2hgenetotable(filename):
    global h2hbase
    with open(filename,'r') as inputfile:
        for element in inputfile:
            if element.find("#")!=0:
                biglist.append(H2H_gene_structs(element.split('\t')))
                # h2hbase+=int(biglist[-1].inf[17])-int(biglist[-1].inf[16])+1
                break
        for element in inputfile:
            biglist.append(H2H_gene_structs(element.split('\t')))
            # h2hbase+=int(biglist[-1].inf[17])-int(biglist[-1].inf[16])+1