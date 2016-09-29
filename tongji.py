# coding=utf-8
import optparse
import sys
import time

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-12'
Dicts={}
conter=0
with open('Homo_sapiens.new') as inputfile:
    with open('singleH2H','w') as outfile:
        for item in inputfile:
            item=item.split('\t')
            if not item[6] in Dicts:
                Dicts[item[6]]=''
                conter+=1
                outfile.write(item[4]+'\t'+item[7]+'\t'+item[8]+'\n')
            if not item[10] in Dicts:
                Dicts[item[10]]=''
                conter+=1
                outfile.write(item[4]+'\t'+item[11]+'\t'+item[12]+'\n')

print(conter)