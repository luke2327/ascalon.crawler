# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JobItem(scrapy.Item):
    job_name = scrapy.Field()
    job_name_ko = scrapy.Field()
    job_class = scrapy.Field()
    main_stat = scrapy.Field()
    main_atk = scrapy.Field()
    wp_type = scrapy.Field()
    assist_wp_type = scrapy.Field()
    affiliation = scrapy.Field()
    create_tmp = scrapy.Field()

    def initialize(self, value):
        for keys, _ in self.fields.items():
            self[keys] = value