# coding=utf-8
import optparse
import sys
import time
from matplotlib import pyplot
import numpy as np
import loopdomain
import seaborn

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-09'
geneexpression={}

Posgenefoldchange=[[],[],[]]
Neggenefoldchange=[[],[],[]]

loopdomain.readloopfile('Primed_loops.txt')
def B_Search(looplist, blockPos):
    end=len(looplist)-1
    start=0
    media=(start+end)//2
    while start != media:
        if looplist[media].start<blockPos:
            if  looplist[media].end> blockPos:
                return media
            else:
                start=media
        else:
            end=media
        media=(start+end)//2
    return -1

def overlaborcontain(chrom,gene,Start,End):
    Outside=2
    Overlab=0
    Contain=1

    if gene[chrom] in loopdomain.loopdict:
        Pos1=B_Search(loopdomain.loopdict[gene[chrom]],int(gene[Start]))
        if Pos1==-1:
            Pos2=B_Search(loopdomain.loopdict[gene[chrom]],int(gene[End]))
            if Pos2!=-1:
                return Overlab
        elif loopdomain.loopdict[gene[chrom]][Pos1].end>int(gene[End]):
            return Contain
        else:
            return Overlab
    return Outside

with open("gene-expression.txt") as inputfiles:
    for gene in inputfiles:
        gene=gene.split('\t')
        geneexpression[gene[1]]=float(gene[5])
with open('H2Hgeneall.c') as H2Hgene:
    with open('H2Hgeneall'+'genenotfindinexpression','w') as notfind:
        for h2h in H2Hgene:
            h2h=h2h.strip()
            h2h1=h2h.split('\t')
            Posgene=h2h1[2].split('@')[0]
            Neggene=h2h1[2].split('@')[1]
            if (Posgene in geneexpression) and (Neggene in geneexpression):
                Pos=overlaborcontain(0,h2h1,3,4)
                Posgenefoldchange[Pos].append(geneexpression[Posgene])
                Neggenefoldchange[Pos].append(geneexpression[Neggene])
            else:
                notfind.write(h2h+'\n')
# number=len(Posgenefoldchange)
# print(number)
x_0=np.array(Posgenefoldchange[0])
y_0=np.array(Neggenefoldchange[0])
x_1=np.array(Posgenefoldchange[1])
y_1=np.array(Neggenefoldchange[1])
x_2=np.array(Posgenefoldchange[2])
y_2=np.array(Neggenefoldchange[2])
x=np.array([Posgenefoldchange[0],Neggenefoldchange[0]])
# pyplot.subplot(2,2,3)
# seaborn.jointplot(x_0,y_0,kind='kde')
# seaborn.lmplot(x='Pos_gene',y='Neg_gene',data=x)
# seaborn.regplot(x=x_2,y=y_2)
# seaborn.jointplot(x_0,y_0,kind='kde')
pyplot.scatter(x_0,y_0,s=50,color='r')
# pyplot.scatter(x_1,y_1,s=50,marker='.',color='g')

# pyplot.scatter(x_2,y_2,marker='v',color='y')
pyplot.title('H2H gene located in Primed hSEC CTCF loop anchor sites')
pyplot.xlabel('Pos_gene fold change')
pyplot.ylabel('Pos_gene fold change')
pyplot.show()