# coding=utf-8
import optparse
import sys
import time
import H2H_structs
import pcgene
import loopdomain

__author__ = 'Guoliang Lin'
Softwarename = 'h2h_hits_loops'
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-18'

Genomeleth=3095693981

def printinformations():
    print("%s software version is %s in %s" % (Softwarename, version, __date__))
    print(bugfixs)
    print('Starts at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def programends():
    print('Ends at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def _parse_args():
    """Parse the command line for options."""
    usage = 'usage: %prog -i input_file -h h2h_file -o output_file'
    parser = optparse.OptionParser(usage)
    parser.add_option('-i',
                      '--input', dest='input', type='string',
                      help='input file ')
    parser.add_option('-g','--h2h',dest='h2h_file',type='string',help='input h2h gene file')
    #    parser.add_option('-v','--variation', dest='variation', type='string', help='input variation information file')
    #    parser.add_option('-g', '--gff3', dest='gff', help='gff3 file')
    parser.add_option('-o', '--output', dest='output', type='string', help='output file')
    options, args = parser.parse_args()
    # positional arguments are ignored
    return options

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


def overlaborcontain(chrom,genelist,Start,End):
    Overlab=0
    Contain=0
    Total=0
    base=0
    for gene in genelist:
        if gene.inf[chrom] in loopdomain.loopdict:
            Total+=1
            Pos1=B_Search(loopdomain.loopdict[gene.inf[chrom]],int(gene.inf[Start]))
            if Pos1==-1:
                Pos2=B_Search(loopdomain.loopdict[gene.inf[chrom]],int(gene.inf[End]))
                if Pos2!=-1:
                    Overlab+=1
                    base=base+int(gene.inf[End])-loopdomain.loopdict[gene.inf[chrom]][Pos2].start+1
            elif loopdomain.loopdict[gene.inf[chrom]][Pos1].end>int(gene.inf[End]):
                Contain+=1
                base=base+int(gene.inf[End])-int(gene.inf[Start])+1
            else:
                Overlab+=1
                base=base+loopdomain.loopdict[gene.inf[chrom]][Pos1].end-int(gene.inf[Start])+1
    return Overlab,Contain,Total,base


def main():
    printinformations()
    # your coding here
    options=_parse_args()

    loopdomain.readloopfile('GSE63525_HUVEC_HiCCUPS_looplist.txt')
    H2H_structs.readh2hgenetotable('singleH2H')
    Overlab,Contain,Total,base=overlaborcontain(0,H2H_structs.biglist,1,2)
    # ratio=base/H2H_structs.h2hbase
    pcgene.readh2hgenetotable('humangenes')
    Overlab,Contain,Total,base=overlaborcontain(0,pcgene.PClist,3,4)
    ratio=base/pcgene.genebase
    print(Overlab,Contain,Total)
    print(Overlab/Total,Contain/Total,(Overlab+Contain)/Total)
    # print(ratio)
    programends()


if __name__ == '__main__':
    sys.exit(main())
