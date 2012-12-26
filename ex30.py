#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex30.py
#:Synopsis: ex30.py
#:Date: 2012-12-26
#:Version: 1.0
#:Author: lovvvve
#:Options: 


people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We cant's decide."

if buses > cars:
    print "That's to many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
