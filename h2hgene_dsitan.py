# coding=utf-8
import optparse
import sys
import time
import numpy as np
from matplotlib import pyplot
import seaborn as sns
from scipy import stats
__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-12'
list1=[]
list2=[]
with open('Homo_sapiens') as inputfile:
    for item in inputfile:
        item=item.split('\t')
        list1.append(int(item[7])-int(item[12]))
with open('Homo_sapiens.new') as inputfile:
    for item in inputfile:
        item=item.split('\t')
        list2.append(int(item[7])-int(item[12]))
data=np.array(list1)
data2=np.array(list2)
print(np.median(data))
print(np.median(data2))
# data=pd.Series(data,name='distance from positive-strand gene TSS')
sns.distplot(data2,bins=100,hist=False)
sns.distplot(data,bins=100,color='r',hist=False)
pyplot.xlabel("Distance from positive-strand gene TSS",fontsize=15)
pyplot.ylabel("Percentage %",fontsize=15)
# pyplot.annotate('Old database',xy=(800,0.0016),xytext=(1050,0.0017),arrowprops=dict(width=3,headwidth=0,headlength=1,facecolor='r'))
pyplot.show()
print('t-statistic = %6.3f pvalue = %6.4f' % stats.ttest_ind(data, data2))

