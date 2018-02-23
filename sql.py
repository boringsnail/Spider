# -*- coding: utf-8 -*-
import json
import MySQLdb
with open("zhihu.json","r") as load_f:
	load_dict = json.load(load_f)

cxn = MySQLdb.connect(host ='localhost',user = 'root',passwd ='1234' ,db ='zhihu')
cur = cxn.cursor()
cur.execute('CREATE TABLE ZhiHu(title VARCHAR(255),zan VARCHAR(255),name VARCHAR(255))')
for i in range(len(load_dict)):
	cur.execute("INSERT INTO title VALUES('%s','%s','%s')") % (load_dict[i]['title'][0],load_dict[i]['zan'][0],load_dict[i]['name'][0])
cur.execute(SELECT *)
for data in cur.fetchall():
	print ('%s\t%s' %data)

