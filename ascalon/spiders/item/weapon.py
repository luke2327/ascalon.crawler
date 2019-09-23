# -*- coding: utf-8 -*-

import logging
import scrapy
import re
from ascalon.items.item import WeaponItem
from ascalon.lib.exception import commonException as ex
from ascalon.lib.stdout.extractEncoding import ExtractEncoding as Encode

class ItemWeaponSpider (scrapy.Spider):
    name = 'item_weapon'
    start_urls = [
        'weapons/one-handed-sword',
        'weapons/two-handed-sword',
        'weapons/one-handed-axe',
        'weapons/two-handed-axe',
        'weapons/one-handed-blunt-weapon',
        'weapons/two-handed-blunt-weapon',
        'weapons/bow',
        'weapons/crossbow',
        'weapons/claw',
        'weapons/dagger',
        'weapons/spear',
        'weapons/polearm',
        'weapons/wand',
        'weapons/staff',
        'weapons/knuckle',
        'weapons/gun',
        'weapons/katara',
        'weapons/dual-bow',
        'weapons/cannon',
    ]
    url_scheme = 'https://global.hidden-street.net/eq/'
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(self.url_scheme + url, self.parse, dont_filter=True)
    def parse(self, response):
        logging.info(response)
        item_cate = response.url.split('/')[-1]
        if item_cate == 'one-handed-sword':
            item_cate = 52
        elif item_cate == 'two-handed-sword':
            item_cate = 63
        elif item_cate == 'one-handed-axe':
            item_cate = 66
        elif item_cate == 'two-handed-axe':
            item_cate = 67
        elif item_cate == 'one-handed-blunt-weapon':
            item_cate = 51
        elif item_cate == 'two-handed-blunt-weapon':
            item_cate = 62
        elif item_cate == 'bow':
            item_cate = 34
        elif item_cate == 'crossbow':
            item_cate = 38
        elif item_cate == 'claw':
            item_cate = 37
        elif item_cate == 'dagger':
            item_cate = 39
        elif item_cate == 'spear':
            item_cate = 59
        elif item_cate == 'polearm':
            item_cate = 53
        elif item_cate == 'wand':
            item_cate = 64
        elif item_cate == 'staff':
            item_cate = 60
        elif item_cate == 'knuckle':
            item_cate = 47
        elif item_cate == 'gun':
            item_cate = 43
        elif item_cate == 'katara':
            item_cate = 68
        elif item_cate == 'dual-bow':
            item_cate = 41
        elif item_cate == 'cannon':
            item_cate = 44
        
        for node in response.xpath('//div[@id="content-content"]//div[contains(@class, "views-row")]'):
            item = WeaponItem()
            # item 전체 초기화
            item.initialize(None)

            xp_first = lambda x: node.xpath('div/table/' + x).extract_first()
            xp = lambda x: node.xpath('div/table/' + x).extract()

            item['item_cate'] = item_cate

            # item 이미지 링크
            try:
                item['image_link'] = xp_first('tr[1]/td[1]/img/@src')
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            # item 영어 이름
            try:
                item['name'] = xp_first('tr[1]/td[2]/strong/text()').strip()
            except ex.IgnoreType as e:
                logging.error(e)
                continue
            
            # item 요구 레벨
            try:
                item['req_level'] = xp('tr[1]/td[3]/text()')[0].strip()
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            # item 요구 스탯
            try:
                req_all_stat = xp('tr[1]/td[4]/text()')[0].strip()
                if req_all_stat == '-':
                    item['req_str'] = 0
                    item['req_dex'] = 0
                    item['req_int'] = 0
                    item['req_luk'] = 0
                else:
                    req_all_stat = req_all_stat.split(', ')
                    for stat in req_all_stat:
                        item['req_' + re.findall(r'(\w+)', stat.split()[0])[0].lower()] = stat.split()[1]
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            # item 공격력 / 마력 / 기본 옵션
            try:
                w1 = ''
                w2 = ''
                w3 = ''

                w1_type = ''
                w2_type = ''
                w3_type = ''
                try:
                    w1 = xp('tr[2]/td[1]/div[1]/text()')[0].split('(')[0].strip()
                    w1_type = xp('tr[2]/td[1]/div[1]/strong/text()')[0].strip().lower()
                except IndexError:
                    pass
                try:
                    w2 = xp('tr[2]/td[1]/div[2]/text()')[0].split('(')[0].strip() 
                    w2_type = xp('tr[2]/td[1]/div[2]/strong/text()')[0].strip().lower()
                except IndexError:
                    pass
                try:
                    w3 = xp('tr[2]/td[1]/div[3]/text()')[0].split('(')[0].strip()
                    w3_type = xp('tr[2]/td[1]/div[3]/strong/text()')[0].strip().lower()
                except IndexError:
                    pass
                
                # 공격력도 마력도 없는데 wdef 옵션이 붙는 경우는 없으므로 패스
                if 'weapon att' in w1_type:
                    item['watk'] = w1
                elif 'magic att' in w1_type:
                    item['matk'] = w1
                
                if 'weapon_att' in w2_type:
                    item['watk'] = w2
                elif 'magic att' in w2_type:
                    item['matk'] = w2
                elif 'weapon def' in w2_type:
                    w2 = w2.split(',')
                    for wdef in w2:
                        if 'speed' in wdef.lower():
                            item['speed'] = re.findall(r'(\d+)', wdef)[0].strip()
                        elif 'jump' in wdef.lower():
                            item['jump'] = re.findall(r'(\d+)', wdef)[0].strip()
                if 'weapon_att' in w3_type:
                    item['watk'] = w3
                elif 'magic att' in w3_type:
                    item['matk'] = w3
                elif 'weapon def' in w3_type:
                    w3 = w3.split(',')
                    for wdef in w3:
                        if 'speed' in wdef.lower():
                            item['speed'] = re.findall(r'(\d+)', wdef)[0].strip()
                        elif 'jump' in wdef.lower():
                            item['jump'] = re.findall(r'(\d+)', wdef)[0].strip()
            except ex.IgnoreType as e:
                logging.error(e)
                continue
                
            # item 공격 속도 / 내구도
            try:
                item_etc = xp('tr[2]/td[2]/text()')
                item_etc_type = xp('tr[2]/td[2]/strong/text()')



                if len(item_etc_type) == 2:
                    for etc in item_etc_type:
                        if 'durability' in etc.lower():
                            item['durability'] = item_etc[1].strip()
                        elif 'speed' in etc.lower():
                            item['atk_speed'] = re.findall(r'(\d+)', item_etc[3])[0].strip()
                else:
                    item['atk_speed'] = re.findall(r'(\d+)', item_etc[1])[0].strip()
            except (IndexError, ex.IgnoreType) as e:
                item['atk_speed'] = 0
                item['durability'] = 0
                logging.error(e)
                continue
            
            # item 클래스
            try:
                item['item_class'] = xp('tr[2]/td[3]/text()')[0].strip().replace(' ', '').lower()
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            # item 순수 능력치
            try:
                item_effect = xp('tr[3]/td[1]/text()')[0].split(',')
                for eff in item_effect:
                    if 'accuracy' in eff.lower():
                        item['acc'] = re.findall(r'\+(\d+)', eff)[0].strip()
                    elif 'avoidability' in eff.lower():
                        item['avoid'] = re.findall(r'\+(\d+)', eff)[0].strip()
                    elif '-' not in eff:
                        item[re.findall(r'(\w+)', eff.split()[0])[0].lower()] = re.findall(r'\+(\d+)', eff)[0].strip()
            except ex.IgnoreType as e:
                logging.error(e)
                continue

            # item 업그레이드 가능 횟수
            try:
                item['upgrade_slot'] = xp('tr[3]/td[2]/text()')[0].strip()
                if item['upgrade_slot'] == '-':
                    item['upgrade_slot'] = '0'
            except ex.IgnoreType as e:
                logging.error(e)
                continue
            
            yield item