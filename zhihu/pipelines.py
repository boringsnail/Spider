# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuPipeline(object):
	def __init__(self,dbpool):
		self.dbpool = dbpool
	@classmethod
	def from_settings(cls,settings):
		dbparams = dict(
			host = setings['localhost'],
			db = setings['zhihu'],
			user = settings['root'],
			passwd = settings['1234'],
			charset = 'utf8',
			cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
			)
		dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
        return cls(dbpool)
	def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
		query.addErrback(self._handle_error, item, spider)
       	return item
	def _conditional_insert(self, tx, item):
		sql = "insert into jsbooks(author,title,url,pubday,comments,likes,rewards,views) values(%s,%s,%s,%s,%s,%s,%s,%s)"
		params = (item['name'], item['title'], item['zan'])
		tx.execute(sql, params)
	def _handle_error(self, failue, item, spider):
		print failue