import argparse
#from glob import glob
#from find_ngrams import pull_lines,print_sequence_matches,sequence_matcher_to_dataframe,save_dataframe
from find_ngrams import process_input
#from tabulate import tabulate



parser=argparse.ArgumentParser(prog='ngraminator',
                    description='If output_file is missing, print to terminal instead. Paths to directories will match all files in that directory.',
                    epilog='')
parser.add_argument("first_files")
parser.add_argument("second_files")
parser.add_argument("output_file",nargs='?',default=None)
parser.add_argument('--cutoff',default=4,type=int,help="cutoff. Only matches >=cutoff will be found. Defaults to 4 characters")
parser.add_argument('--filetype',default='excel',choices=["excel","csv"],help="output filetype. Defaults to excel.")
parser.add_argument('--separators',default=None,help="specify a file with a list of separators to override the default list. Should contain a single line, and each character on that line will be used.")
args=parser.parse_args()

first_files = args.first_files
second_files = args.second_files

if first_files[-1] == "/":
    first_files += "*" #help glob work in an intuitive way
if second_files[-1] == "/":
    second_files += "*"

if args.separators == None:
    separators = ['，','。','；','？','「','」','：','！','《','》','、','．']
else:
    f=open(args.separators,'r')
    separators=list(f.readline())
    f.close()

process_input(first_files,second_files,args.output_file,args.cutoff,separators,args.filetype)

#a_lines,a_map = pull_lines(glob(first_files),separators=separators)
#b_lines,b_map = pull_lines(glob(second_files),separators=separators)

#df = sequence_matcher_to_dataframe(a_lines,b_lines,a_map,b_map,cutoff=args.cutoff)
#if args.output_file == None:

#    print(tabulate(df, showindex=False, headers=df.columns)) #going back and forth on this, but if you add ,disable_numparse=True it'll left-justify the length
#else:
#    save_dataframe(df,args.output_file,format=args.filetype)
