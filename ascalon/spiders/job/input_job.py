# -*- coding: utf-8 -*-

import logging
import scrapy
import datetime
import re
from dateutil.parser import parse
from ascalon.items.job import JobItem
from ascalon.lib.exception import commonException as ex
from ascalon.lib.stdout.extractEncoding import ExtractEncoding as Encode

class JobMapleSpider (scrapy.Spider):
    name = 'job_maple'
    start_urls = [
        "http://maplestory.nexon.net/game/classes-jobs", # 모험가-전사 2019-09-22 by liam
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, dont_filter=True)

    def parse(self, response):
        logging.info(response)
        scheme = 'http://maplestory.nexon.net'
        for node in response.xpath('//li[contains(@class, "jobclass-item")]'):
            item = JobItem()

            # item 전체 초기화
            item.initialize(None)

            xp = lambda x: node.xpath(x).extract()[0]

            item['job_class'] = xp('@class').split()[1]

            url = scheme + xp('div[@class="photo"]/a/@href')

            try:
                yield scrapy.Request(url, meta={'item': item}, callback=self.parse_job)
            except Exception as e:
                print(e)

    def parse_job(self, response):
        item = response.meta['item']

        xp = lambda x: response.xpath(x).extract()[0]

        job_type = re.findall(r'(\w+)', response.xpath('//li[@class="key-item"]/ul/li/text()').extract()[0])[0]

        if (job_type.strip() == 'EXPLORER'):
            job_type = ''
            return None

        item['job_name'] = xp('//h1[@class="title"]/text()')
        item['main_stat'] = re.findall(r'\((.*)\)', response.xpath('//li[@class="key-item"]/ul/li/text()').extract()[1])[0]
        item['affiliation'] = job_type

        if (item['job_name'] == 'Xenon'):
            item['main_stat'] = 'STR, DEX, LUK'

        if (item['main_stat'] == 'INT'):
            item['main_atk'] = 'magical'
        else:
            item['main_atk'] = 'physical'

        return item
