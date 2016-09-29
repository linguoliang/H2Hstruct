# coding=utf-8
import optparse
import sys
import time
import H2H_structs
import math
__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-08'

H2H_structs.readh2hgenetotable('Homo_sapiens.new')
with open('H2Hgeneoverlap.c','w') as outoverlap:
    with open('H2Hgenenooverlap.c','w') as outnooverlap:
        with open('H2Hgeneall.c','w') as allgene:
            for H2H in H2H_structs.biglist:
                assert isinstance(H2H,H2H_structs.H2H_gene_structs)
                if H2H.isoverlab():
                    outoverlap.write(H2H.inf[4]+'\t'+H2H.getcenter()+'\t'+H2H.inf[3]+'\t'+H2H.inf[16]+'\t'+H2H.inf[17]+'\n')
                else:
                    outnooverlap.write(H2H.inf[4]+'\t'+H2H.getcenter()+'\t'+H2H.inf[3]+'\t'+H2H.inf[16]+'\t'+H2H.inf[17]+'\n')
                allgene.write(H2H.inf[4]+'\t'+int(H2H.getnegstart())+ (int(H2H.getposend())+int(H2H.getposstart()))+'\t'+H2H.inf[3]+'\t'+H2H.inf[16]+'\t'+H2H.inf[17]+'\n')