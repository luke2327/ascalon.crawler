# -*- coding: utf-8 -*-

import logging
import scrapy
from ascalon.items.maple_news import NoticeItem
from ascalon.lib.exception import commonException as ex
from ascalon.lib.stdout.extractEncoding import ExtractEncoding as Encode

class NoticeMapleKMS (scrapy.Spider):
    name = 'notice_maple_kms'
    start_urls = ["https://maplestory.nexon.com/News/Notice"]
    url_scheme = 'https://maplestory.nexon.com/'

    def start_requests(self):
        for pageIndex in range(1, 11):
            yield scrapy.Request(
                self.start_urls[0] + '?page=' + str(pageIndex),
                self.parse,
                dont_filter=True
            )

    def parse(self, response):
        logging.info(response)

        print 'connect... start' + str(response)

        for node in response.xpath('//div[@class="news_board"]/ul/li'):
            item = NoticeItem()

            # item 전체 초기화
            item.initialize(None)

            xp = lambda x: node.xpath(x).extract_first()

            item['region'] = 'KMS'

            try:
                item['link'] = self.url_scheme + xp('p/a/@href')

                print item['link']
            except IndexError as e:
                logging.error(e)

                continue

            try:
                item['title'] = xp('p/a/span/text()')

                print item['title']
            except (IndexError, ex.IgnoreType) as e:
                logging.error(e)

                continue

            try:
                iconType = xp('p/a/em/img/@src').split('/')[-1]
                print iconType
                iconAlt = xp('p/a/em/img/@alt')

                if ('icon01' in iconType and u'공지' in iconAlt):
                    item['type'] = u'공지'
                elif ('icon02' in iconType and u'GM소식' in iconAlt):
                    item['type'] = u'GM소식'
                elif ('icon03' in iconType and u'점검' in iconAlt):
                    item['type'] = u'점검'

            except (IndexError, ex.IgnoreType) as e:
                logging.error(e)

                continue

            try:
                item['published_date'] = xp('div/dl/dd/text()')
            except (IndexError, ex.IgnoreType) as e:
                logging.error(e)

                continue

            yield scrapy.Request(
                item['link'],
                meta={'item': item},
                callback=self.parse_deep
            )

    def parse_deep(self, response):
        item = response.meta['item']

        item['desc'] = ' '.join(response.xpath('//div[@class="new_board_con"]//*').extract())

        return item