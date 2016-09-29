# coding=utf-8
import optparse
import sys
import time

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-21'

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-19'
global genebase
genebase=0
PClist=[]
class PC_gene_structs:
    '''
    这个类是用来存储gene 的信息

    '''
    def __init__(self,listinf):
        self.inf=listinf



def readh2hgenetotable(filename):
    global genebase
    with open(filename,'r') as inputfile:
        for element in inputfile:
            if element.find("#")!=0:
                PClist.append(PC_gene_structs(element.split('\t')))
                genebase+=int(PClist[-1].inf[4])-int(PClist[-1].inf[3])+1
                break
        for element in inputfile:
            PClist.append(PC_gene_structs(element.split('\t')))
            genebase+=int(PClist[-1].inf[4])-int(PClist[-1].inf[3])+1