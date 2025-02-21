# ngraminator
A tool for running ngram analyses, mostly geared towards Chinese texts. Pick two texts (or two collections of texts),
specify the minimum n-gram overlap you'd like, and let it rip.

### Installation and usage.  

Download or clone. The only package you may also need to install is ```tkinter```, and that only if you want to use the gui.

Command line use: ```ngramminator first_files second_files output_file```. If output_file is missing, print the results to the terminal instead -- this can be useful if you're doing initial tests. For either file position, Passing a path to a directory will match all files in that directory, while passing a single filename will match only to that file. It's possible (and often desirable) to look for matches from one file against a range of others.

Options:   
--cutoff  Only matches >=cutoff will be found. Defaults to 4 characters
--filetype Can be 'excel' (.xlsx) or 'csv'. Defaults to excel.  
--separators Allows you to specify a file with a list of separators to override the default list. Should contain a single line, and each character on that line will be used. By default, there is a set of common punctuation that ngramminator will automatically strip out. 



### Usage hints

### Caveats

This is still an experimental project! It seems to work pretty well, but use at your own risk.

Important caveat: I made this for my partner because she cares a lot about textual parallelism. Rather than  tweak filenames for her each time, I've put it together in a handy little package so she could do it herself as needed. *I do not know Classical Chinese. I am literally Searle's [Chinese Room](https://en.wikipedia.org/wiki/Chinese_room) here.*
