# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VodItem(scrapy.Item):
    title = scrapy.Field()
    game = scrapy.Field()
    source = scrapy.Field()
    link = scrapy.Field()
    duration = scrapy.Field()
    image_link = scrapy.Field()
    del_field = scrapy.Field()
    create_tmp = scrapy.Field()