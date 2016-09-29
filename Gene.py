# coding=utf-8
import optparse
import sys
import time

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-07'

GeneDict={}

class Gene:
    """
    用来存储基因的信息，包括基因名，scaffold,以及起始和终止位点
    """

    def __init__(self, listitems, genename, geneId):
        """
        init values
        """
        assert isinstance(listitems, list)
        assert isinstance(genename, str)
        self.scaffold = listitems[0]
        self.start = int(listitems[3])
        self.end = int(listitems[4])
        self.genename = genename
        self.geneId = geneId


def readgtf(filename):
    number=0
    with open(filename) as file:
        for items in file:
            item=items.split('\t')
            if item[1]=="protein_coding" and item[2]=='gene':
                number=number+1
                tmp = item[8].split(';')
                genename = tmp[1].split(' ')[2].replace('"', '')
                geneid = tmp[0].split(' ')[1].replace('"', '')
                tmgene = Gene(item[0:5], genename,geneid)
                if tmgene.scaffold in GeneDict:
                    GeneDict[tmgene.scaffold].append(tmgene)
                else:
                    GeneDict[tmgene.scaffold]=[tmgene]
        print(number)