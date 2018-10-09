# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .db import DB
class ProxyipPipeline(object):
    def process_item(self, item, spider):
        item_dict=dict(item)
        db=DB('proxy_ip',**item_dict)
        db.insert()
        return item
