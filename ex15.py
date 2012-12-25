#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex15.py
#:synopsis: ex15.py
#:Date: 2012-12-20
#:Version: 1.0
#:Author: lovvvve
#:Options: 


from sys import argv

script,filename = argv

txt=open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the file again:"
file_again = raw_input(">")

txt_again=open(file_again)

print txt_again.read()
