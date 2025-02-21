import argparse
from find_ngrams import process_input

default_separators = ['，','。','；','？','「','」','：','！','《','》','、','．']


parser=argparse.ArgumentParser(prog='ngraminator',
                    description='If output_file is missing, print to terminal instead. Paths to directories will match all files in that directory.',
                    epilog='')
parser.add_argument("first_files",nargs='?',default=None)
parser.add_argument("second_files",nargs='?',default=None)
parser.add_argument("output_file",nargs='?',default=None)
parser.add_argument('--cutoff',default=4,type=int,help="cutoff. Only matches >=cutoff will be found. Defaults to 4 characters")
parser.add_argument('--filetype',default='excel',choices=["excel","csv"],help="output filetype. Defaults to excel.")
parser.add_argument('--separators',default=None,help="specify a file with a list of separators to override the default list. Should contain a single line, and each character on that line will be used.")
parser.add_argument('--print_separators',action='store_true', help="Print the default list of separators and quit.")
args=parser.parse_args()


if args.print_separators:
    print(" ".join(default_separators))
    exit()

first_files = args.first_files
second_files = args.second_files

if first_files==None or second_files==None:
    parser.print_help()
    exit()

if first_files[-1] == "/":
    first_files += "*" #help glob work in an intuitive way
if second_files[-1] == "/":
    second_files += "*"

if args.separators == None:
    separators = default_separators
else:
    f=open(args.separators,'r')
    separators=list(f.readline())
    f.close()

process_input(first_files,second_files,args.output_file,args.cutoff,separators,args.filetype)
