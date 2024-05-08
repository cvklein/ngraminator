import difflib
from collections import Counter
import itertools
import pandas as pd

#these are the standard chinese text separators that I've been using. here as default
separators = ['，','。','；','？','「','」','：','！','《','》','、','．']

def splitline(line, separators=['，','。','；','？','「','」','：','！','《','》','、','．']):
    for s in separators:
        line = " ".join(line.split(s))
    return [x for x in line.split(' ') if x != '']

def sequence_cleaner(rlist):   #this eliminates sequences that are contained in smaller sequences by iteratively comparing
    removeset = set()
    for a,b in itertools.combinations(rlist,2):
        if len(a) == len(b):
            pass
        elif len(a) > len(b):
            try:
                _ = a.index(b)
                removeset.add(b)
            except ValueError:
                pass
        else:
            try:
                _ = b.index(a)
                removeset.add(a)
            except ValueError:
                pass
    return list(set(rlist) - removeset)

def brute_sequence_matcher(a,b,min_length):
    done = False
    matchlen = min_length
    rlist = []
    while not done:
        done = True
        for start in range(0,len(a)-matchlen):
            comp = a[start:start+matchlen]
            try:
                _ = b.index(comp)
                rlist.append(comp)
                done = False
            except ValueError:
                pass
        matchlen += 1
    return sequence_cleaner(list(set(rlist)))


def pull_lines(filenames): #pull strings from a list of filenames, and also return a dictionary mapping line to filenames
    if type(filenames) == str:   #allow to pass single filename
        filenames = [filenames]

    lineno = 0
    line_to_file = {}
    return_lines = []

    for filename in filenames:
        base_filename = filename.split('/')[-1]
        f = open(filename,'r')
        for line in f:
            line = line.replace('\n','')
            if line == "":
                pass
            elif line[0].isdigit():
                pass
            else:
                return_lines.append("".join(splitline(line)))
                line_to_file[lineno] = base_filename
                lineno += 1
    return return_lines,line_to_file


def print_sequence_matches(a_lines,b_lines,a_map,b_map,cutoff=4): #print out matches; this is for testing.
    for x in range(len(a_lines)):
        for y in range(len(b_lines)):
            rlist = brute_sequence_matcher(a_lines[x],b_lines[y],cutoff)
            for entry in rlist:
                oline = " ".join([a_map[x],b_map[y],entry,str(len(entry))])
                print(oline)

def sequence_matcher_to_dataframe(a_lines,b_lines,a_map,b_map,cutoff=4): #return a dataframe with sequences
    amaps,bmaps,entries,len_es = [],[],[],[]  #probably a better way to build a datafram?
    for x in range(len(a_lines)):
        for y in range(len(b_lines)):
            rlist = brute_sequence_matcher(a_lines[x],b_lines[y],cutoff)
            for entry in rlist:
                amaps.append(a_map[x])
                bmaps.append(b_map[y])
                entries.append(entry)
                len_es.append(str(len(entry)))
    df = pd.DataFrame()
    df['a_file'] = amaps
    df['b_file'] = bmaps
    df['match'] = entries
    df['len'] = len_es
    return df

def save_dataframe(df,filename,format='xlsx'):
    if format == 'excel':
        df.to_excel(filename+'.xlsx',index=False)
    else:
        df.to_csv(filename+'.csv',index=False)
