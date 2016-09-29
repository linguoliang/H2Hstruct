# coding=utf-8
import re

__author__ = 'Guoliang Lin'
Softwarename = ''
version = '1.0.1'
bugfixs = ''
__date__ = '2016-09-09'

'''
#pairID 0	species 1	Tax_id 2	PosSymbol_NegSymbol 3	chromosome 4	PosSymbol 5	PosGeneID 6	PosStart 7
    PosStop 8	NegSymbol 9	NegGeneID 10	NegStart 11	NegStop 12	TssDist 13	DistClass 14	BlockLength 15
    BlockStart 16	BlockStop 17	PosSynonyms 18	NegSynonyms 19
'''

length=1000

genomeDict = {}
pairID = 0
with open('Homo_sapiens.GRCh37.75.gtf') as inputfile:
    with open('Homo_sapiens.new', 'w') as outputfile:
        for i in range(8):
            inputfile.readline()
        for strinf in inputfile:
            listinf = strinf.split('\t')
            if strinf.find('#') != 0:
                if listinf[2] == 'gene' and listinf[1] == "protein_coding" and (
                            listinf[0] == 'Y' or listinf[0] == 'X' or re.match('\D.*', strinf) == None):
                    if listinf[0] in genomeDict:
                        genomeDict[listinf[0]][listinf[6]].append(listinf)
                    else:
                        genomeDict[listinf[0]] = {'+': [], '-': []}
                        genomeDict[listinf[0]][listinf[6]].append(listinf)
        for chrom in genomeDict:
            genomeDict[chrom]['-'].sort(key=lambda x: int(x[4]))
            genomeDict[chrom]['+'].sort(key=lambda x: int(x[3]))
            for Ngene in genomeDict[chrom]['-']:
                flag=False
                for Pgene in genomeDict[chrom]['+']:
                    if abs(int(Ngene[4]) - int(Pgene[3])) <= length:
                        flag=True
                        tmpn = Ngene[8].split(';')
                        tmpp = Pgene[8].split(';')
                        geneidp = tmpp[0].split(' ')[1].replace('"', '')
                        genenamep = tmpp[1].split(' ')[2].replace('"', '')
                        geneidn = tmpn[0].split(' ')[1].replace('"', '')
                        genenamen = tmpn[1].split(' ')[2].replace('"', '')
                        Tax_id = geneidp + '_' + geneidn
                        PosSymbol_NegSymbol = genenamep + '@' + genenamen
                        BlockStart = min(int(Ngene[3]), int(Ngene[4]), int(Pgene[3]), int(Pgene[4]))
                        BlockStop = max(int(Ngene[3]), int(Ngene[4]), int(Pgene[3]), int(Pgene[4]))
                        BlockLength = BlockStop - BlockStart + 1

                        outputfile.write(str(
                            pairID) + '\tHomo_sapiens' + '\t' + Tax_id + '\t' + PosSymbol_NegSymbol + '\t' + chrom + '\t' + genenamep + '\t' + geneidp + '\t' +
                                         Pgene[3] + '\t' + Pgene[4] + '\t' + genenamen + '\t' + geneidn + '\t' + Ngene[
                                             3] + '\t' + Ngene[4] + '\t' + str(pairID) + '\t' + str(
                            pairID) + '\t' + str(BlockLength) + '\t' + str(BlockStart) + '\t' + str(BlockStop) + '\t' + str(
                            pairID) + '\t' + str(pairID) + '\n')
                        pairID+=1
                    elif flag:
                        break

