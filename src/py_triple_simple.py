#!/usr/bin/python
"""
    By default loads a ntriples file into a in-memory triple store
    and performs basic statistics on the resulting ntriple file
"""


import time
import sys
import os
import pprint

import pyTripleSimple

def main(ntriples_file_name,display_n=50):

    if display_n == "All":
        display_n = None
    else:
        display_n=int(display_n)

    f = open(ntriples_file_name,"r")

    ts = pyTripleSimple.SimpleTripleStore() #pyTripleSimple.ShelveTripleEngine(ntriples_file_name)
    
    print('Loading "%s"' % os.path.abspath(ntriples_file_name))
    start_time = time.clock()
    ts.load_ntriples(f)
    end_time = time.clock()
    print("Finished loading ntriples file")
    
    number_of_triples = ts.n_triples()
    
    print("Number of triples %s loaded in %s seconds (%s triples/second)" % (number_of_triples, end_time - start_time,(number_of_triples * 1.0)/ (end_time - start_time)))
    print("Number of distinct lexical symbols: %s" % ts.n_symbols())
    
    print("Number of distinct subjects: %s" % ts.n_subjects())
    print("Number of distinct predicates: %s" % ts.n_predicates())
    print("Number of distinct objects including literals: %s" % ts.n_objects())
    print("Number of literals: %s" % ts.n_literals())
    print("")
    print("Top subjects are:")
    pprint.pprint(ts.top_subjects(display_n))
    print("")
    print("Top objects are:")
    pprint.pprint(ts.top_objects(display_n))
    print("")
    print("Top predicates are:")
    pprint.pprint(ts.top_predicates(None))

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        main("reach.nt")
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1],sys.argv[2])