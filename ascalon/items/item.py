# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    name = scrapy.Field()
    name_ko = scrapy.Field()
    item_cate = scrapy.Field()
    req_level = scrapy.Field()
    req_str = scrapy.Field()
    req_dex = scrapy.Field()
    req_int = scrapy.Field()
    req_luk = scrapy.Field()
    all_stat = scrapy.Field()
    str = scrapy.Field()
    dex = scrapy.Field()
    int = scrapy.Field()
    luk = scrapy.Field()
    hp = scrapy.Field()
    mp = scrapy.Field()
    maxhp = scrapy.Field()
    maxmp = scrapy.Field()
    watk = scrapy.Field()
    matk = scrapy.Field()
    wdef = scrapy.Field()
    mdef = scrapy.Field()
    speed = scrapy.Field()
    jump = scrapy.Field()
    acc = scrapy.Field()
    avoid = scrapy.Field()
    durability = scrapy.Field()
    available = scrapy.Field()
    item_class = scrapy.Field()
    upgrade_slot = scrapy.Field()
    image_link = scrapy.Field()

    def initialize(self, value):
        for keys, _ in self.fields.items():
            self[keys] = value

class WeaponItem(Item):
    atk_speed = scrapy.Field()
    boss_dmg = scrapy.Field()
    ignore_def = scrapy.Field()

class EquipItem(Item):
    ignore_def = scrapy.Field()

class AccessoriesItem(Item):
    pass