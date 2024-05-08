import argparse
from find_ngrams import pull_lines,print_sequence_matches,sequence_matcher_to_dataframe,save_dataframe


parser=argparse.ArgumentParser(prog='ngraminator',
                    description='Usage ngraminator firstfiles secondfiles outputfile',
                    epilog='')
parser.add_argument("first_files")
parser.add_argument("second_files")
parser.add_argument("output_file")
args=parser.parse_args()

print(args.first_files)
print(args.second_files)
print(args.output_file)
