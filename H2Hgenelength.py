# coding=utf-8
'''
评估H2H基因的分布
'''
import optparse
import sys
import time
import matplotlib
from matplotlib import pyplot
import H2H_structs
import numpy
import seaborn as sns
import pandas as pd

lengthDic=[]
__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-08'
H2H_structs.readh2hgenetotable('Homo_sapiens')
for H2H in H2H_structs.biglist:
    assert isinstance(H2H,H2H_structs.H2H_gene_structs)
    lengthDic.append(int(H2H.inf[15]))
a=min(lengthDic)
b=max(lengthDic)
data=numpy.array(lengthDic)
print(a,numpy.median(data),b)
sns.distplot(data,bins=200,kde=False,rug=True,color='r')
# pyplot.hist(data,bins=60,range=(0,500000),color="red")
pyplot.xlabel('nihap',fontsize=34)
pyplot.show()