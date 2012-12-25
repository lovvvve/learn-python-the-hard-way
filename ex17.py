#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex17.py
#:synopsis: ex17.py
#:Date: 2012-12-25
#:Version: 1.0
#:Author: lovvvve
#:Options: 


from sys import argv
from os.path import exists

scripts,from_file,to_file=argv

print "Copying from %s to %s" %(from_file,to_file)

# we could do these two on one line too, how?
in_file=open(from_file)
indata=in_file.read()

print "The input file is %d byte long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready,hit RETURN to contiue,CTRL-C to abort."
raw_input()
out_file=open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close
in_file.close
