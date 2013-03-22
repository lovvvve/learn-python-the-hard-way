#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex34.py
#:Synopsis: ex34.py
#:Date: 2012-12-27
#:Version: 1.0
#:Author: lovvvve
#:Options: 


#动物园跑步比赛结果查询
animals=['乌龟','熊','蟒蛇','孔雀','袋鼠','兔子','狮子']

print "动物园跑步比赛结果查询!"
print "请输入要查询的名次(1-6):",
rank=int(raw_input())

print "第%d名的动物是:%s" %(rank,animals[rank-1])

