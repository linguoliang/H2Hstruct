# coding=utf-8
'''
    本文件用于从H2HDB中提取特定物种的h2h基因用于后续分析
'''
import optparse
import sys
import time

__author__ = 'Guoliang Lin'
Softwarename = 'substract_from_h2hdb'
version = '1.0.1'
bugfixs = ''
__date__ = '2016-07-18'


def printinformations():
    print("%s software version is %s in %s" % (Softwarename, version, __date__))
    print(bugfixs)
    print('Starts at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def programends():
    print('Ends at :' + time.strftime('%Y-%m-%d %H:%M:%S'))


def _parse_args():
    """Parse the command line for options."""
    usage = 'usage: %prog -i input_file -s species_name -o output_file'
    parser = optparse.OptionParser(usage)
    parser.add_option('-i',
                      '--input', dest='input', type='string',
                      help='input file')
    parser.add_option('-s','--species',dest='species',type='string',help='input species name')
    #    parser.add_option('-v','--variation', dest='variation', type='string', help='input variation information file')
    #    parser.add_option('-g', '--gff3', dest='gff', help='gff3 file')
    parser.add_option('-o', '--output', dest='output', type='string', help='output file')
    options, args = parser.parse_args()
    # positional arguments are ignored
    return options


def main():
    printinformations()
    # your coding here
    options=_parse_args()
    with open(options.input,'r') as inputfile:
        with open(options.output,'w') as outputfiles:
            head=inputfile.readline().split('\t')  #trim head file
            for item in inputfile:
                if item.find(options.species)!=-1:
                    outputfiles.write(item)
    programends()


if __name__ == '__main__':
    sys.exit(main())
