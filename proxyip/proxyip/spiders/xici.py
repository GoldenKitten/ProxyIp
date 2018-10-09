#!/usr/bin/python
#coding:utf-8

"""
@author: GoldenKitten
@contact: GoldenKitten@163.com
@software: PyCharm
@file: xici.py
@time: 2018/10/8 21:03
"""
import scrapy
from ..items import ProxyipItem
class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = [
        'http://www.xicidaili.com/',
    ]
    def start_requests(self):
        reqs=[]
        for i in range(1,5):
            req=scrapy.Request('http://www.xicidaili.com/nn/%s'%i)
            reqs.append(req)
        return reqs
    def parse(self, response):
        ip_list=response.xpath('//table[@id="ip_list"]')
        trs=ip_list[0].xpath('tr')
        items=[]
        for tr in trs[1:]:
            pre_item=ProxyipItem();
            pre_item['IP']=tr.xpath('td[2]/text()')[0].extract()
            pre_item['PORT'] = tr.xpath('td[3]/text()')[0].extract()
            pre_item['POSITION'] = tr.xpath('td[4]/a/text()')[0].extract()
            pre_item['TYPE'] = tr.xpath('td[6]/text()')[0].extract()
            pre_item['SPEED'] = tr.xpath('td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
            pre_item['LAST_CHECKTIME'] = tr.xpath('td[10]/text()')[0].extract()
            items.append(pre_item)
        return items
if __name__ == "__main__":
	pass
