#!/usr/bin/env python



import json
from math import log
from sys import argv



USAGE = '''%s <class 1 counts> <class 2 counts> [class i counts ...] \
<query tokens file>'''



if __name__ == '__main__':
    if len(argv) < 4:
        print USAGE % argv[0]
        exit(1)

    classes = argv[1:-1]
    classcounts = []
    queryf_tokens = None

    with open(argv[-1]) as queryf:
        queryf_tokens = json.load(queryf)

    for classcountsf in classes:
        with open(classcountsf) as cf:
            classcounts.append(json.load(cf))

    classtotals = [ cc['total_examples'] for cc in classcounts ]
    classlogs = [ log(ct) - log(sum(classtotals)) for ct in classtotals ]

    for token in queryf_tokens:
        for i in xrange(len(classlogs)):
            classlogs[i] += log(classcounts[i].get(token, 1)) - \
                            log(classtotals[i])

    result = { 'file' : argv[-1],
               'chosen_class' : classlogs.index(max(classlogs))
             }
    
    for i,cl in enumerate(classlogs):
        result['c%d' % i] = cl

    print json.dumps(result)
