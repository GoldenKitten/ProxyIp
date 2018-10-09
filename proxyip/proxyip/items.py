# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    IP = scrapy.Field()  # ip地址
    PORT = scrapy.Field()  # 端口
    POSITION = scrapy.Field()  # 位置
    TYPE = scrapy.Field()  # 类型
    SPEED = scrapy.Field()  # 速度
    LAST_CHECKTIME = scrapy.Field()  # 核查时间
