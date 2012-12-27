#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex33.py
#:Synopsis: ex33.py
#:Date: 2012-12-27
#:Version: 1.0
#:Author: lovvvve
#:Options: 


i=0
numbers=[]

while i<6:
    print"i的值是: %d" %i
    numbers.append(i)

    i+=1
    print "列表number现在是:",numbers


print "The numbers:"

for num in numbers:
    print num
