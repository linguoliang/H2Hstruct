# coding=utf-8
import optparse
import sys
import time
import re

__author__ = 'Guoliang Lin'
Softwarename = 'getgene'
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-21'


def printinformations():
    print("%s software version is %s in %s" % (Softwarename, version, __date__))
    print(bugfixs)
    print('Starts at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def programends():
    print('Ends at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def _parse_args():
    """Parse the command line for options."""
    usage = 'usage: %prog -i FILE.bcf -g FILE.gff3 -o OUTPREFIX'
    parser = optparse.OptionParser(usage)
    parser.add_option('-i',
                      '--input', dest='input', type='string',
                      help='input file ')
    #    parser.add_option('-f','--fpkm',dest='fpkm_file',type='string',help='input fpkm file')
    #    parser.add_option('-v','--variation', dest='variation', type='string', help='input variation information file')
    #    parser.add_option('-g', '--gff3', dest='gff', help='gff3 file')
    parser.add_option('-o', '--output', dest='output', type='string', help='output file')
    options, args = parser.parse_args()
    # positional arguments are ignored
    return options



def main():
    printinformations()
    options=_parse_args()
    with open(options.input) as inputfile:
        with open(options.output,'w') as outputfile:
            for i in range(8):
                inputfile.readline()
            for strinf in inputfile:
                listinf=strinf.split('\t')
                if strinf.find('#')!=0:
                    if listinf[2] =='gene' and listinf[1]=="protein_coding" and re.match('\D.*',strinf)==None:
                        outputfile.write(strinf)

    programends()


if __name__ == '__main__':
    sys.exit(main())
