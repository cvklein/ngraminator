import argparse
from glob import glob
from find_ngrams import pull_lines,print_sequence_matches,sequence_matcher_to_dataframe,save_dataframe


parser=argparse.ArgumentParser(prog='ngraminator',
                    description='Usage ngraminator first_files second_files output_file',
                    epilog='')
parser.add_argument("first_files")
parser.add_argument("second_files")
parser.add_argument("output_file")
parser.add_argument('--cutoff',default=4,type=int,help="cutoff. Only matches >=cutoff will be found. Defaults to 4 characters")
args=parser.parse_args()

first_files = args.first_files
second_files = args.second_files

if first_files[-1] == "/":
    first_files += "*" #help glob work in an intuitive way
if second_files[-1] == "/":
    second_files += "*"

a_lines,a_map = pull_lines(glob(first_files))
b_lines,b_map = pull_lines(glob(second_files))

df = sequence_matcher_to_dataframe(a_lines,b_lines,a_map,b_map,cutoff=args.cutoff)
save_dataframe(df,args.output_file)
