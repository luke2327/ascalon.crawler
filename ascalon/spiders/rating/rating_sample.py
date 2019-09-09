import logging
import scrapy
from ascalon.items.rating import RatingItem

class RatingSampleSpider(scrapy.Spider):
    name = 'rating_sample'
    start_urls = ["http://lol.inven.co.kr/dataninfo/ladder/",]
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, dont_filter=True)
    def parse(self, response):
        for node in response.xpath('//div[@class="ladderTable"]'
                                   '//tr[2 <= position() and position() < 51]'):
            item = RatingItem()
            xp = lambda x: node.xpath(x).extract()[0]
            try:
                item['player_name'] = xp('td[2]/a/text()')
            except Exception:
                continue
            item['link'] = xp('td[2]/a/@href')
            item['rank'] = xp('td[1]/div[@class="crank"]/text()')
            item['source'] = 'inven.co.kr'
            item['game'] = 'LOL'
            print item
            # yield item
