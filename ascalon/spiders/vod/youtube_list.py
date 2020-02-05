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
        # maplestory
        "https://www.youtube.com/channel/UCiCNc3uj8Bnc9bDzHJS058Q/videos", # 신해조 2019-09-17 by liam
        "https://www.youtube.com/channel/UCR0aLp4aIvxS07g6rGWZr_g/videos", # 개구릿대 2019-10-06 by liam
        "https://www.youtube.com/channel/UC1dHu9GhbHH7RcHKyJdaOvA/videos", # 맑음 2019-10-06 by liam
        "https://www.youtube.com/channel/UCk5C4AR3uvmKwZYkIlSobbg/videos", # 한자 2019-10-06 by liam
        "https://www.youtube.com/user/skswhdkgo/videos", # 세글자 2019-10-06 by liam
        "https://www.youtube.com/user/mlchoins/videos", # 명예훈장 2019-10-06 by liam
        "https://www.youtube.com/user/bjpange/videos", # 팡이 2019-10-06 by liam
        "https://www.youtube.com/channel/UChYtqPBdX9xTFGKV0tFrtgg/videos", # 루니오 2020-01-23 by liam
    ]
    url_scheme = 'youtube.com'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, dont_filter=True)

    def parse(self, response):
        logging.info(response)
        auth = response.xpath('//meta[@name="title"]/@content').extract()[0]
        path = response.url.split('/')[-2]
        lang = 'ko'

        for node in response.xpath('//li[contains(@class, "yt-shelf-grid-item")]/div/div'):
            item = VodItem()

            # item 전체 초기화
            item.initialize(None)
            xp_first = lambda x: node.xpath(x).extract_first()
            xp = lambda x: node.xpath(x).extract()

            item['source'] = 'youtube.com'
            item['game'] = 'maple'

            try:
                item['auth'] = auth
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            try:
                item['language_cd'] = lang
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            try:
                item['title'] = xp_first('div[@class="yt-lockup-content"]/h3/a/@title')
                if item['title'] is None:
                    raise ex.IgnoreType('title', item['title'])
            except (IndexError, ex.IgnoreType) as e:
                logging.error(e)
                continue

            try:
                item['link'] = self.url_scheme + xp_first('div[@class="yt-lockup-content"]/h3/a/@href')
            except IndexError as e:
                logging.error(e)
                continue

            try:
                temp_hits = re.findall(r'(\d+)', xp('div[@class="yt-lockup-content"]/div/ul/li[1]/text()')[0])
                temp_hits = ''.join(temp_hits)

                item['hits'] = temp_hits
            except Exception as e:
                logging.error(e)
                continue

            try:
                item['before_tmp'] = xp('div[@class="yt-lockup-content"]/div/ul/li[2]/text()')[0]
                time = item['before_tmp'].split()[0]
                method = item['before_tmp'].split()[1]
                current_time = datetime.datetime.now()

                delta = ''

                if 'second' in method:
                    delta = datetime.timedelta(seconds=int(time))
                elif 'hour' in method:
                    delta = datetime.timedelta(hours=int(time))
                elif 'day' in method:
                    delta = datetime.timedelta(days=int(time))
                elif 'week' in method:
                    delta = datetime.timedelta(weeks=int(time))
                elif 'month' in method:
                    delta = datetime.timedelta(days=int(time * 30))

                if delta != '':
                    item['create_tmp'] = current_time - delta
            except IndexError as e:
                logging.error(e)

            try:
                item['duration'] = ''
                temp_duration = xp_first('div[@class="yt-lockup-thumbnail"]/span[contains(@class,'\
                                    '"contains-addto")]/span[@class="video-time"]/span/@aria-label')
                if temp_duration is None:
                    raise ex.IgnoreType('duration', temp_duration)
                temp_duration = temp_duration.split(',')

                # initlize with timedelta
                delta_hours = datetime.timedelta(hours = 0)
                delta_minutes = datetime.timedelta(minutes = 0)
                delta_seconds = datetime.timedelta(seconds = 0)
                for time in temp_duration:
                    time.strip()
                    if 'second' in time:
                        delta_seconds = datetime.timedelta(seconds = int(time.split()[0]))
                    elif 'minute' in time:
                        delta_minutes = datetime.timedelta(minutes = int(time.split()[0]))
                    elif 'hour' in time:
                        delta_hours = datetime.timedelta(hours = int(time.split()[0]))
                delta_duration = str(delta_hours + delta_minutes + delta_seconds)

                dt = []
                for time in delta_duration.split(':'):
                    dt.append(str(int(time)))

                # join duration
                item['duration'] = dt[0] + 'h ' + dt[1] + 'm ' + dt[2] + 's'
            except ex.IgnoreType as e:
                logging.error(e)
                continue
            except Exception as e:
                print e

            ############
            ## CUSTOM ##
            ############

            # 팡이
            if path == 'bjpange':
                if u'메이플스토리' not in item['title']:
                    continue

            ## if you insert video that first time
            ## should on below line
            # item['del_field'] = 1

            # Encode(object=item)

            yield item
