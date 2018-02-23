# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import ZhihuItem
class zhihuSpider(scrapy.Spider):
	name = "zhihu"
	allowed_domains = ['sogou.com/']
	start_urls = [
	'http://zhihu.sogou.com/']
	def parse(self,response):
		sel = scrapy.selector.Selector(response)
		# names = sel.xpath('//div/div/div/div/ul/li/div/div/p[@class="p1"]/a/text()').extract()
		# zans = sel.xpath('//div/div/div/div/ul/li/div/div/p/span/text()').extract()
		# titles = sel.xpath('//div/div/div/div/ul/li/p/a/text()').extract()
		sites = sel.xpath('//div/div/div/div/ul[@class="news-list"]/li')
		items = []
		for site in sites:
			item = ZhihuItem()
			item['name'] = site.xpath('div/div/p[@class="p1"]/a/text()').extract()
			item['zan'] = site.xpath('div/div/p/span/text()').extract()
			item['title'] = site.xpath('p/a/text()').extract()
			items.append(item)
		return items