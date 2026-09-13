# ngraminator
A tool for running ngram analyses, specifically geared towards classical Chinese texts. Pick two texts, or two collections of texts, specify the minimum n-gram overlap you'd like, and let it rip. You'll get back a file with the corresponding filenames for each text, the length of the overlap, and the overlap itself.

Ngraminator works pretty hard to give the largest non-overlapping matches it can find. So if a text has AAABBB and another text has AAABB it will return AAABB but *not* AA, AAB, etc.

### Installation and usage.  

Download or clone. The only package you may also need to install is ```tkinter```, and that only if you want to use the gui.

Command line use: ```ngramminator first_files second_files output_file```

If output_file is missing, print the results to the terminal instead -- this can be useful if you're doing initial tests. For either file position, Passing a path to a directory will match all files in that directory, while passing a single filename will match only to that file. It's possible (and often desirable) to look for matches from one file against a range of others.

Options:   
```-h``` or ```--help``` Print usage information    
```--cutoff```  Only matches >=cutoff will be found. Defaults to 4 characters   
```--filetype``` Type of output file. Can be 'excel' (.xlsx) or 'csv'. Defaults to excel.  
```--separators``` This allows you to specify a file with a list of separators to override the default list. Should contain a single line.  Each character on that line will be used.    
```--print_separators``` Print the default list of separators and quit.   

If you want to use the GUI, just run (either from the terminal or by double-clicking ```ngraminator_gui.py```). Usage is the same as above, though you can't select new separators this way and you must output to file.



### Usage hints

Ngramminator wants plain text files. You should make sure that the encoding used in both files is the same; it will not match characters across different encodings.

Ngramminator cares about newlines, and shouldn't match across them. If you're getting weird results, make sure your text is split up the way you'd like it to be.



The code to find the largest non-overlapping match has a bit of a brute force component. This doesn't matter that much because Chinese texts are pretty small and  computers are fast. However, if you put in a single big file (say, the entire *Shiji*) it can take upwards of a few minutes to run. It will look hung while it runs. It's a good time for a cup of tea. Or you can split your file up into smaller chapters; in general, smaller files are much faster.

By default, there is a set of common punctuation characters that ngramminator will automatically strip out before doing the comparison. If you're getting unexpected results, try using the ```---separators``` option with a handmade file of the stuff you want to get rid of.

Ngramminator will ignore the entire line if it begins with an Arabic numeral,  on the assumption that these are later additions. If you need these, use the ```--preserve_digit_lines``` flag (only available from command line)



### Caveats


This is still an experimental project! It seems to work pretty well, but use at your own risk.

Important caveat: *I do not know Classical Chinese. I am literally Searle's [Chinese Room](https://en.wikipedia.org/wiki/Chinese_room) here.* I made this for my partner because she cares a lot about textual parallelism. Rather than tweak filenames for her each time, I've put the original code together in a handy  package so she play with it herself as needed.

13 Sep 2026: I finally made this public! Feedback very welcome


### Still todo:
- Split larger texts automatically in the background to keep things snappy.   
- Implement a progress bar.
- Let GUI output to screen for testing


###  License, Citation, Contact information

This software is released under the GNU General Public License version 3 (GPL3.0) [https://opensource.org/licenses/GPL-3.0](https://opensource.org/licenses/GPL-3.0)   

If you use this package, I'd appreciate a citation -- for now, just mention the package and let me know about it.

I can be reached at cvklein@gmail.com. Thanks to Esther Klein for years of beta testing.
