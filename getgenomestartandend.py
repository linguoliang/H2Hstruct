# coding=utf-8
'''
获取基因的起始位点和终止位点
'''
import optparse
import sys
import time
import random

geneIddict={}
__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-09'
with open('Homo_sapiens.new') as geneidfile:
    for element in geneidfile:
        element=element.split('\t')
        geneIddict[element[6]]=''
        geneIddict[element[10]]=''
with open('humangenes') as inputfile:
    with open('humangenestart','w') as genestart:
        with open('humangeneends','w') as geneends:
            with open('humangeneall','w') as geneall:
                with open('randomsite','w') as randomsite:
                    for item in inputfile:
                        item=item.strip()
                        listitem=item.split('\t')
                        geneId=listitem[8].split(';')[0].split(' ')[1].replace('"', '')
                        if geneId not in geneIddict:
                            if listitem[6]=='+':
                                genestart.write(listitem[0]+'\t'+listitem[4]+'\t'+listitem[3]+'\t'+listitem[4]+'\n')
                            else:
                                geneends.write(listitem[0]+'\t'+listitem[4]+'\t'+listitem[3]+'\t'+listitem[4]+'\n')
                            randomsite.write(listitem[0]+'\t'+str(random.randint(int(listitem[3]),int(listitem[4])))+'\t'+listitem[3]+'\t'+listitem[4]+'\n')
                            geneall.write(listitem[0]+'\t'+listitem[4]+'\t'+listitem[3]+'\t'+listitem[4]+'\n')