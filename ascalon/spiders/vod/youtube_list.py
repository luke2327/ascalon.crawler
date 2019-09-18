# -*- coding: utf-8 -*-

import logging
import scrapy
import datetime
import re
from dateutil.parser import parse
from ascalon.items.vod import VodItem
from ascalon.lib.exception import commonException as ex
from ascalon.lib.stdout.extractEncoding import ExtractEncoding as Encode

class VodYoutubeMapleSpider (scrapy.Spider):
    name = 'vod_youtube_maple'
    start_urls = [
        "https://www.youtube.com/channel/UCiCNc3uj8Bnc9bDzHJS058Q/videos", # 신해조 2019-09-17 by liam
    ]
    url_scheme = 'youtube.com'
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, dont_filter=True)
    def parse(self, response):
        logging.info(response)
        for node in response.xpath('//li[contains(@class, "yt-shelf-grid-item")]/div/div'):
            item = VodItem()
            xp = lambda x: node.xpath(x).extract_first()

            item['source'] = 'youtube.com'
            item['game'] = 'maple'

            try:
                item['title'] = xp('div[@class="yt-lockup-content"]/h3/a/@title')
                if item['title'] is None:
                    raise ex.IgnoreType('title', item['title'])
            except (IndexError, ex.IgnoreType) as e:
                logging.error(e)
                continue

            try:
                item['link'] = self.url_scheme + xp('div[@class="yt-lockup-content"]/h3/a/@href')
            except IndexError as e:
                logging.error(e)
                continue
            
            try:
                temp_duration = xp('div[@class="yt-lockup-thumbnail"]/span[contains(@class, "contains-addto")]/span[@class="video-time"]/span/@aria-label')
                temp_duration = re.split(r',', temp_duration)
                print temp_duration

                dt_hours = '0'
                dt_minutes = '0'
                dt_seconds = '0'
                for time in temp_duration:
                    time.strip()
                    if 'seconds' in time:
                        dt_seconds = time.split()[0]
                    elif 'minutes' in time:
                        dt_minutes = time.split()[0]
                    elif 'hours' in time:
                        dt_hours = time.split()[0]
                print dt_seconds
                temp_duration = str(parse(dt_hours + ':' + dt_minutes + ':' + dt_seconds)).split()[1]
                # duration_dt = datetime.datetime.strftime()
                item['duration'] = temp_duration
                
                print item['duration']
                print '\n'
            except Exception as e:
                print e

            # Encode(location = 'duration', object = item['duration'])