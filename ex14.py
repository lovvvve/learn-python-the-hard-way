#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex14.py
#:synopsis: ex14.py
#:Date: 2012-12-20
#:Version: 1.0
#:Author: lovvvve
#:Options: 


from sys import argv

script,user_name=argv
prompt='>'

print "Hi %s, I'm the %s script." %(user_name,script)
print "I'd like to ask you a few quertion."
print "Do you like me %s" %user_name
likes = raw_input(prompt)

print "Where do you live %s" %user_name
lives=raw_input(prompt)

print "What kind of computer do you have?"
computer=raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes,lives,computer)
