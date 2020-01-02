# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsBase(scrapy.Item):
    title = scrapy.Field()
    published_date = scrapy.Field()
    desc = scrapy.Field()
    region = scrapy.Field()
    link = scrapy.Field()
    create_tmp = scrapy.Field()

    def initialize(self, value):
        for keys, _ in self.fields.items():
            self[keys] = value

class NoticeItem(NewsBase):
    type = scrapy.Field()

class UpdateItem(NewsBase):
    pass