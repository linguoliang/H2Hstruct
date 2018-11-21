# coding=utf-8
'''
评估SMC1 CTCF Enhancer 在cron区域两侧分布
'''
import optparse
import sys
import time
#import os.re
import numpy as np
from matplotlib import pyplot
import seaborn as sns
import pandas as pd
from scipy import stats
import matplotlib

binsize=5000

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-08'
elementDict={}
listdis=[]
star=0
end=0
listdisn=[]
elementpath='Primed_CTCF_center.txt'

H2Hpath='singleH2H.c'
Normal='humangeneall'
with open(elementpath) as elmet:
    for item in elmet:
        item=item.strip()
        tmp=item.split('\t')
        if tmp[0] in elementDict:
            elementDict[tmp[0]].append(int(tmp[1]))
        else:
            elementDict[tmp[0]]=[int(tmp[1])]
    for x in elementDict:
        assert isinstance(elementDict[x],list)
        elementDict[x].sort()
with open(H2Hpath) as h2hgen:
    for item in h2hgen:
        item=item.strip()
        tmp=item.split('\t')
        pos=int(tmp[1])
        if tmp[0] in elementDict:
            star=pos-binsize
            end=pos+binsize
            for element in elementDict[tmp[0]]:
                if star<element<end:
                    listdis.append(element-pos)
with open(Normal) as norml:
    for item in norml:
        item=item.strip()
        tmp=item.split('\t')
        pos=int(tmp[1])
        if tmp[0] in elementDict:
            star=pos-binsize
            end=pos+binsize
            for element in elementDict[tmp[0]]:
                if star<element<end:
                    listdisn.append(element-pos)
data=np.array(listdis)
datab=np.array(listdisn)
# pyplot.hist(data,bins=100)
data=pd.Series(data,name='distance from center')
pyplot.hist(data,bins=10)
# x=sns.distplot(data,bins=100,color='r',hist=False)
# y=sns.distplot(datab,bins=100,color='g',hist=False)
# pyplot.xlim((-4000,4000))
# m=range(-4,5)
# ticks=[x*1000 for x in m]
# stringlist=[str(x)+"k" for x in m]
# print(stringlist)
# pyplot.xticks(ticks,stringlist)
# pyplot.legend([x,y],("H2H genes","All genes"),"best", numpoints=1)
pyplot.xticks(range(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
form=matplotlib.ticker.AutoMinorLocator(n=3)
x=pyplot.tick_params()
print(x)
pyplot.show()
print('t-statistic = %6.3f pvalue = %6.4f' % stats.ttest_ind(data, datab))
print('t-statistic = %6.3f pvalue = %6.4f' % stats.ranksums(data,datab))
stats.ranksums(data,datab)