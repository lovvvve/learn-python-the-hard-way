#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: ex32.py
#:Synopsis: ex32.py
#:Date: 2012-12-27
#:Version: 1.0
#:Author: lovvvve
#:Options: 


the_count=[1,2,3,4,5]
fruits=['苹果','橘子','梨','杏']
change=['1','一毛',2,'一块',3,'一百']

#这第一种for循环遍历一个列表
for number in the_count:
    print "This is count %d" % number

#同上
for fruit in fruits:
    print "A fruit of type: %s" %fruit

#我们也可以通过混合名单
# 我们必须使用%r,因为我们不知道里面是什么
for i in change:
    print "I got %r" %i

#我们也可以建立列表，首先启动了一个空的
elements=[]

#使用范围的函数做0到5计数
for i in range(0,6):
    print "Adding %d to the list." %i
    print "123"
    #将数字加入到列表里面
    elements.append(i)

#现在我们可以打印出来了
for i in elements:
    print "Element was:%d" %i
