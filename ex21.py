#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex21.py
#:Synopsis: ex21.py
#:Date: 2012-12-26
#:Version: 1.0
#:Author: lovvvve
#:Options: 


def add(a,b):
    print "ADDING %d+%d" %(a,b)
    return a+b

def subtract(a,b):
    print "SUBTRACTING %d-%d" %(a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLYING %d*%d" %(a,b)
    return a*b

def divide(a,b):
    print "DIVIDE %d/%d" %(a,b)
    return a/b


print "Let's do spme math with just fuctions!"

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print "Age: %d, Hight: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)


#A puzzle for the extra credit,type it in anyway
print "Here is a puzzle."

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you di it ny hand?"
