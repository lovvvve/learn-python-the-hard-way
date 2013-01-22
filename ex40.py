#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex40.py
#:Synopsis: ex40.py
#:Date: 2013-01-23
#:Version: 1.0
#:Author: lovvvve
#:Options: 


class Song(object):
    
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_asong(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_asong()

bulls_on_parade.sing_me_asong()
