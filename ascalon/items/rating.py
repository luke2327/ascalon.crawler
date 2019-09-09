# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RatingItem(scrapy.Item):
    player_name = scrapy.Field()
    game = scrapy.Field()
    source = scrapy.Field()
    rank = scrapy.Field()
    link = scrapy.Field()
    del_field = scrapy.Field()
    create_tmp = scrapy.Field()
