#!/usr/bin/env python



from random import shuffle
from sys import argv



USAGE = '''%s <class JSON files> <class> <list of files to pick splits>'''




if __name__ == '__main__':
    if len(argv) < 4:
        print USAGE % argv[0]
        exit(1)

    files = argv[3:]
    classes = argv[1]
    theclass = argv[2]
    shuffle(files)

    print '#!/bin/bash'
    print '/home/ubuntu/nbayes/nbayes_counter.py ',
    for fname in files[1:int(len(files)*0.50)]:
        print '%s ' % fname,

    print '>> %s_counts.json' % theclass
    for fname in files[int(len(files)*0.50):]:
        print '/home/ubuntu/nbayes/nbayes_decider.py %s %s >> %s_results.json' % (classes, fname, theclass)
