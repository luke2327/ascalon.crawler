# -*- coding: utf-8 -*-
import logging
import sys
import re
import datetime
import random
from scrapy.utils.project import get_project_settings
from ascalon.lib.timezone.tzinfo import TZINFO
settings = get_project_settings()

class AscalonDefault(object):
    reload(sys)
    sys.setdefaultencoding('utf8')
    def __init__(self, idb, item, spider):
        query = idb.dbpool.runInteraction(
            self.conditional_insert, item)
        # query.addErrback(idb.handle_error)
    def _preprocessing(self, item):
        if 'title' in item:
            item['title'] = item['title'].\
                replace('"', "'").\
                replace('^', '').\
                replace('&#8220;', "'").\
                replace('&#8221;', "'").\
                replace('&#8220', "'").\
                replace('&#8221', "'").\
                replace('&#8211', '-').\
                replace(';', ',').\
                replace('}', ']').\
                replace('{', '[').\
                replace(u'???', '-')
        try:
            if 'image_link' in item and item['image_link'] is None:
                item['image_link'] = ''
        except KeyError:
            item['image_link'] = ''
        try:
            if 'del_field' in item and item['del_field'] is None:
                item['del_field'] = '0'
        except KeyError:
            item['del_field'] = '0'
        try:
            if 'create_tmp' in item and item['create_tmp'] is None:
                if 'lang' in item and item['lang'] == 'ko':
                    item['create_tmp'] = datetime.datetime.now(TZINFO['KST'])
                elif 'lang' in item and item['lang'] == 'ja':
                    item['create_tmp'] = datetime.datetime.now(TZINFO['JST'])
                else:
                    item['create_tmp'] = datetime.datetime.now(TZINFO['UTC'])
        except KeyError:
            item['create_tmp'] = datetime.datetime.now(TZINFO['UTC'])

        random_second = datetime.timedelta(seconds=int(random.randrange(1,60)))
        fmt = "%Y-%m-%d %H:%M:%S"
        item['create_tmp'] = (item['create_tmp'] + random_second).strftime(fmt)

        return item
    def conditional_insert(self, tx, item):
        pass
