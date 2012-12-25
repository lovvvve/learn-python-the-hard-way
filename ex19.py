#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex19.py
#:synopsis: ex19.py
#:Date: 2012-12-26
#:Version: 1.0
#:Author: lovvvve
#:Options: 


def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for aparty!"
    print "Get a blanket.\n"


print "We can just give the fuction numbers dirctly:"
cheese_and_crackers(20,30)


print "OR,we can use variables from our scripts:"
aaa=10
bbb=50

cheese_and_crackers(aaa,bbb)


print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "aaa=",
aaa=int(raw_input())
print "bbb=",
bbb=int(raw_input())
print "And we can combine the two,variables and math:"
cheese_and_crackers(aaa+100,bbb+1000)
