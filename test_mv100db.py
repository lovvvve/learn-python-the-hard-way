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
par = open('/opt/mypython/commandId_parameter.txt','r')
parlines=par.readlines()
commandId_parlist = []
for line_commandId_par in parlines:
    line_commandId_par=line_commandId_par.strip('\n')
    commandId_parlist.append(line_commandId_par)
#    print commandId_list
par.close()
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
#    print "CommandLine is \"%s\" hashcode is \"%s\" " %(commandLine,hashcodeNu)

    if commandId in commandId_parlist:
        print "%s is insert" %commandId
    else:
        desc_values = "("+"%s,"*13+"%s)"
        sql_parameter = "select id from parse_match_parameter where commandId = '"+commandId+"';"
        n=ytest.execute(sql_parameter)
        if n != 0:
            rows_parameter = ytest.fetchall()
            for row_parameter in rows_parameter:
                print "+"*10
                print "CommandLine is \"%s\" hashcode is \"%s\" " %(commandLine,hashcodeNu)
                print row_parameter[0]
                sql_select_parameter_id = "SELECT * FROM parse_match_keyword WHERE parameterId = '"+row_parameter[0]+"';"
                sql_delete_parameter_id = "DELETE FROM parse_match_keyword WHERE parameterId = '"+row_parameter[0]+"';"
#                print sql_select_parameter_id
                nn = ytest.execute(sql_select_parameter_id)
#                print nn
                if nn != 0:
                    print nn
                    get_select_parameter_datas = ytest.fetchall()
                    conn_nu = MySQLdb.connect (host="127.0.0.1",user="root",passwd="",db=dbn,charset="utf8")
#                    #连接到对应的数据库
                    sql_insert_data="INSERT INTO parse_match_keyword_"+tbNu+" VALUES "+desc_values
                    dbInsert = conn_nu.cursor()
                    outthing=dbInsert.executemany(sql_insert_data,get_select_parameter_datas)
                    ytest.execute(sql_delete_parameter_id)
#                    print outthing
                    conn_nu.commit()
                    conn_test.commit()
                    commandId_parlist.append(commandId)
                    par = open('/opt/mypython/commandId_parameter.txt','a')
                    par.write(commandId)
                    par.write("\n")
                    par.close()
                    print commandId_parlist
#
