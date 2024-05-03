import difflib
from collections import Counter
import itertools

#these are the standard chinese text separators that I've been using. here as default 
separators = ['，','。','；','？','「','」','：','！','《','》','、','．']

def splitline(line, separators=['，','。','；','？','「','」','：','！','《','》','、','．']):
    for s in separators:
        line = " ".join(line.split(s))
    return[x for x in line.split(' ') if x != '']

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


def pullchars(terms):
    bs = []
    for t in terms:
        for tt in t:
            bs.append(tt)
    return bs
