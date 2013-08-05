#!/usr/bin/env python



from json import loads
from sys import argv




USAGE = '''%s <results file> <class>'''
CLASSMAP = { 0 : 'Artemis-Fowl',
             1 : 'Bible',
             2 : 'Fairy-Tales',
             3 : 'Hunger-Games',
             4 : 'Peter-Pan',
             5 : 'Pride-and-Prejudice',
             6 : 'Redwall',
             7 : 'Vampire-Diaries'
           }


if __name__ == '__main__':
    if len(argv) < 3:
        print USAGE % argv[0]
        exit(1)

    total = 0
    true_positives = 0
    true_negatives = 0
    theclass = argv[2]

    for line in open(argv[1]).readlines():
        data = loads(line)

        total += 1

        if CLASSMAP[int(data['chosen_class'])] in data['file'] and \
           CLASSMAP[int(data['chosen_class'])] == theclass:
               true_positives += 1

        if CLASSMAP[int(data['chosen_class'])] not in data['file'] and \
           theclass not in data['file']:
                true_negatives += 1

    accuracy = float(true_positives + true_negatives) / (total)
    print 'Accuracy ((TP + TN) / (TP + FP + FN + TN)) == %0.4f' % accuracy
