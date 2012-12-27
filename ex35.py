#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex35.py
#:Synopsis: ex35.py
#:Date: 2012-12-27
#:Version: 1.0
#:Author: lovvvve
#:Options: 


from sys import exit

def gold_room():
    print "这是一个装满黄金的屋子。你想带走多少呢？"

    next=raw_input("> ")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
        dead("你这个人不识数吧!")

    if how_much<50:
        print "好的，你不贪心，你赢了！"
        exit(0)
    else:
        dead("你是个贪婪的混蛋！")


def bear_room():
    print "这里有熊。"
    print "熊有一堆蜂蜜。"
    print "胖熊在前面的另一个门。"
    print "你该怎样移动熊呢？"
    bear_moved=False

    while True:
        print """
a.拿走蜂蜜
b.嘲讽熊
c.打开门
        """
        next=raw_input("> ")

        if next == "a":
            dead("熊看着你，然后打你的脸了。")
        elif next == "b" and not bear_moved:
            print "熊已经从屋里出来,你可以通过它去了。"
            bear_moved = True
        elif next == "b" and bear_moved:
            dead("你被愤怒的熊咬断了腿。")
        elif next == "c" and bear_moved:
            gold_room()
        else:
            print "我不知道这意味着什么。"


def cthulhu_room():
    print "在这里你看到一个巨大邪恶的恶魔。"
    print "他在一直的盯着你,你快要疯了!"
    print "你是选择逃跑还是让他吃了你?\na.逃跑\nb.还是让恶魔吃了吧!"

    next = raw_input("> ")

    if "a" in next:
        start()
    elif "b" in next:
        dead("这真是好吃！")
    else:
        cthulhu_room()


def dead(why):
    print why,"活该！"
    exit(0)

def start():
    print "现在你在一个漆黑的屋里"
    print "在你的左边和邮编各有一个门"
    print "你会选择打开哪一个呢?\na.左边的\nb.右边的"

    next = raw_input("> ")

    if next == "a":
        bear_room()
    elif next == "b":
        cthulhu_room()
    else:
        dead("你在房间里直到你饿死!")


start()
