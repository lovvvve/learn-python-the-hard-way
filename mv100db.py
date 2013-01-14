#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: mv100db.py
#:Synopsis: mv100db.py
#:Date: 2013-01-10
#:Version: 1.0
#:Author: lovvvve
#:Options: 


import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
import MySQLdb

############################
f = open('/opt/mypython/commandId.txt','r')
rlines=f.readlines()
commandId_list = []
for line_commandId in rlines:
    line_commandId=line_commandId.strip('\n')
    commandId_list.append(line_commandId)
#    print commandId_list
f.close()
###########################从本地文件读取已经处理过的command

conn_test = MySQLdb.connect (host="127.0.0.1",user="root",passwd="",db="yuyicloud_test",charset="utf8")

ytest = conn_test.cursor()
sql="SELECT id,command,hashcode FROM parse_match_command WHERE hashcode <> '0000';" #查出来所有hashcode不是0000的command
ytest.execute(sql)
rows = ytest.fetchall()
#print rows #查看所有的command hashcode 不是0000的
for row in rows: #测试,只看两行
    #print row[0],row[1],row[2]
    commandId = row[0]
    commandLine = row[1]
    hashcodeNu = row[2]
    dbNu=hashcodeNu[:2]
    tbNu=hashcodeNu[2:4]
    insert_db="yuyicloud_"+dbNu
    dbn="yuyicloud_"+dbNu
    #从parse_match_command表中获得相关数据
##################################    
    print "CommandLine is \"%s\" hashcode is \"%s\" " %(commandLine,hashcodeNu)
    if commandId in commandId_list:
        print "%s is insert" %commandId
    else:
        select_tables=["parse_match_context","parse_match_sentence"]
        for select_table in select_tables:
            print "select data from \"%s\"" %select_table
#            #
            desc_sql = "DESC "+select_table+";"
            desc_table_num = ytest.execute(desc_sql)
#            print '%s 表共有 %s 列' %(select_table,desc_table_num)
            desc_values = "("+"%s,"*(desc_table_num-1)+"%s)"
#            print desc_values
#            ####获取列的个数
#            print 'commandId is: "%s"'%commandId
            sql_select_data_test = "SELECT * FROM "+select_table+" WHERE commandId = '"+commandId+"';"
            sql_delete_data_test = "DELETE FROM "+select_table+" WHERE commandId = '"+commandId+"';"
#            print sql_select_data_test
            select_commandId_num = ytest.execute(sql_select_data_test)
            get_select_datas = ytest.fetchall()
#            print "%s 的commandId 是 %s 在 %s 表中共 %s 条。\n" %(commandLine,commandId,select_table,select_commandId_num)
#            print get_select_datas
#            #
#            for get_select_data in get_select_datas:
            if select_commandId_num != 0:
                print "%s 的commandId 是 %s 在 %s 表中共 %s 条。" %(commandLine,commandId,select_table,select_commandId_num)
                conn_nu = MySQLdb.connect (host="127.0.0.1",user="root",passwd="",db=dbn,charset="utf8")
                #连接到对应的数据库
                insert_data="INSERT INTO "+select_table+"_"+tbNu+" VALUES "+desc_values
#                print insert_data
#                print get_select_data
                dbInsert = conn_nu.cursor()
                outthing=dbInsert.executemany(insert_data,get_select_datas)
                conn_nu.commit()
                commandId_list.append(commandId)
                f = open('/opt/mypython/commandId.txt','a')
                f.write(commandId)
                f.write("\n")
                f.close()
                print commandId_list
                ytest.execute(sql_delete_data_test)
                conn_test.commit()
#==========================
    


#def forloop(startn):
#    for i in range(startn,100):
#        print '%02d' % i
#
#
#forloop(1)

