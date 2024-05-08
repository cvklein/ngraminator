import argparse
from glob import glob
from find_ngrams import pull_lines,print_sequence_matches,sequence_matcher_to_dataframe,save_dataframe


parser=argparse.ArgumentParser(prog='ngraminator',
                    description='Usage ngraminator firstfiles secondfiles outputfile',
                    epilog='')
parser.add_argument("first_files")
parser.add_argument("second_files")
parser.add_argument("output_file")
args=parser.parse_args()


a_lines,a_map = pull_lines(glob(args.first_files))
b_lines,b_map = pull_lines(glob(args.second_files))

df = sequence_matcher_to_dataframe(a_lines,b_lines,a_map,b_map,cutoff=4)
save_dataframe(df,args.output_file)
