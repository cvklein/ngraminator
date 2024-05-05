import difflib
from collections import Counter
import itertools

#these are the standard chinese text separators that I've been using. here as default
separators = ['，','。','；','？','「','」','：','！','《','》','、','．']

def splitline(line, separators=['，','。','；','？','「','」','：','！','《','》','、','．']):
    for s in separators:
        line = " ".join(line.split(s))
    return [x for x in line.split(' ') if x != '']

def sequence_cleaner(rlist):   #this eliminates sequences that are contained in smaller sequences
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
        try:  #assign keep track of base filename for line_to_file. try/except done for cases where single file in local dir is passed
            base_filename = filename.split('/')[1].split('.')[0]
        except IndexError:
            base_filename = filename
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
