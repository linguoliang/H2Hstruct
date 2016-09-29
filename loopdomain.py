# coding=utf-8
'''
    用来存储环状结构
'''
import optparse
import sys
import time
from functools import reduce

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-20'


global loopbase
loopbase=0
loopdict={}
class loopstruct:
    '''

    '''

    def __init__(self,char,listinf):
        self.chrom = char
        #tmp=map(lambda x: int(x), listinf)
        self.start = min(map(lambda x: int(x), listinf[0:4]))
        self.end = max(map(lambda x: int(x), listinf[0:4]))
        self.full=listinf[4]


def caculatelooplength():
    length=0
    for key,val in loopdict.items():
        for loop in val:
            assert isinstance(loop,loopstruct)
            length=length+loop.end-loop.start+1
    return length

def initloopdict(element):
    global loopbase
    listinf=element.split('\t')
    if listinf[0] == listinf[3]:
        char=listinf[0]
        listdomain=listinf[1:3]
        listdomain.append(listinf[4])
        listdomain.append(listinf[5])
        listdomain.append(listinf)
        loop=loopstruct(char,listdomain)
        loopbase+=loop.end-loop.start+1
        if loop.chrom in loopdict:
            loopdict[loop.chrom].append(loop)
        else:
            loopdict[loop.chrom]=[loop]

def readloopfile(filename):
    with open(filename,'r') as inputfile:
        for element in inputfile:
            if element.find("#")!=0:
                initloopdict(element)
                break
        for element in inputfile:
            initloopdict(element)
        for chrom in loopdict.keys():
            loopdict[chrom].sort(key=lambda x:x.start)