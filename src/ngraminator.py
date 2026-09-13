import argparse
from find_ngrams import process_input

default_separators = ['，','。','；','？','「','」','：','！','《','》','、','．']

class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        # max_help_position controls the starting column of the description
        # width controls the overall terminal wrap width
        super().__init__(prog, max_help_position=40, width=100)


parser=argparse.ArgumentParser(prog='ngraminator',
                    description='If output_file is missing, print to terminal instead. Paths to directories will match all files in that directory.',
                    epilog='',
                    formatter_class=CustomHelpFormatter)#this plus above allows for better formatting of help options
parser.add_argument("first_files",nargs='?',default=None)
parser.add_argument("second_files",nargs='?',default=None)
parser.add_argument("output_file",nargs='?',default=None)
parser.add_argument('--cutoff',default=4,type=int,help="\t cutoff. Only matches >=cutoff will be found. Defaults to 4 characters")
parser.add_argument('--filetype',default='excel',choices=["excel","csv"],help="output filetype. Defaults to excel.")
parser.add_argument('--separators',default=None,help="specify a file with a list of separators to override the default list. Should contain a single line, and each character on that line will be used.")
parser.add_argument('--print_separators',action='store_true', help="Print the default list of separators and quit.")
parser.add_argument('--preserve_digit_lines', action='store_true',help="Set to keep lines which start with an Arabic numeral (otherwise they're dropped)")

args=parser.parse_args()


if args.print_separators:
    print(" ".join(default_separators))
    exit()

preserve_digit_lines = False
if args.preserve_digit_lines:

    preserve_digit_lines = True
    print('preserving digit lines')

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

process_input(first_files,second_files,args.output_file,args.cutoff,separators,args.filetype,preserve_digit_lines)
