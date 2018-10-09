#!/usr/bin/python
#coding:utf-8

"""
@author: GoldenKitten
@contact: GoldenKitten@163.com
@software: PyCharm
@file: db.py
@time: 2018/10/9 10:50
"""
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,MetaData,Table,UniqueConstraint
from .settings import DB_CONFIG
class DB(object):
	def __init__(self,table_name,**kwargs):
		self.datas=kwargs
		# 本地数据库
		db_user_config = DB_CONFIG['db_user_config']
		db_str = '%s+%s://%s:%s@%s:%s/%s?charset=%s' % (
			DB_CONFIG['db_name'],
			DB_CONFIG['db_driver'],
			db_user_config['user'],
			db_user_config['passwd'],
			db_user_config['host'],
			db_user_config['port'],
			db_user_config['db'],
			db_user_config['charset']
		)
		engine = create_engine(db_str)
		metadata = MetaData()
		temp=[Column('ID',Integer,primary_key=True),]
		for field in kwargs.keys():
			temp.append(Column(field,String(50)))
		self.tb=Table(table_name,metadata,*tuple(temp))
		metadata.create_all(engine)
		# 获取数据库连接
		self.conn = engine.connect()
	def insert(self):
		i=self.tb.insert()
		r=self.conn.execute(i,**self.datas)
if __name__ == "__main__":
	pass
