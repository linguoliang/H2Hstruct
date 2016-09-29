# coding=utf-8
import optparse
import sys
import time
import H2H_structs

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-08'

files='Primed_SMC1'

H2H_structs.readh2hgenetotable('Homo_sapiens')
with open('H2H_Homo_sapiens.bed','w') as outputfile:
    for H2H in H2H_structs.biglist:
        assert isinstance(H2H,H2H_structs.H2H_gene_structs)
        outputfile.write(H2H.returnbedformate()+'\n')
# with open(files) as inputfile:
#     with open(files+'.bed','w') as oputfile:
#         for item in inputfile:
#             tmplist=item.split('\t')
#             if tmplist[0]==tmplist[3]:
#                 tmpstr=tmplist[0].replace('chr','')
#                 oputfile.write(tmpstr+'\t'+tmplist[1]+'\t'+tmplist[5]+'\t'+tmplist[6]+'\n')