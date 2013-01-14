#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex39.py
#:Synopsis: ex39.py
#:Date: 2013-01-05
#:Version: 1.0
#:Author: lovvvve
#:Options: 


#create a papping of state to abbreviation 
states = {
    'Oregon': 'OR',
    'Florida': 'Fl',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# 创建一个基本的州和一些城市在他们
cities = {
    'CA': 'San Francisco',
    'MI': 'Derroit',
    'Fl': 'Jacksonvillea'
}

# 添加更多的城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#打印出一些城市
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#打印一些州
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida hs: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviation %s" % (state,abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

# now do bath at the same time
print '-' * 10
for state,abbrev in states.items():
    print "%s state is abbreviation %s and has city %s" %(
    state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:
    print "Sorry, no Texas."

# get a city with a default valua
city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: %s" % city
