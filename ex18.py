#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex18.py
#:synopsis: ex18.py
#:Date: 2012-12-26
#:Version: 1.0
#:Author: lovvvve
#:Options: 


#this one is like your scripts with argv
def print_two(*args):
    arg1,arg2=args
    print "arg1: %r, arg2: %r" %(arg1,arg2)

#ok, that *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" %(arg1,arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %s" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zen","Shaw")
print_two_again("Zen","Shaw")
print_one("First!")
print_none()
