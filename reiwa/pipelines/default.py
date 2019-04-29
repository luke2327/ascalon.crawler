# -*- coding: utf-8 -*-
import logging
import sys
import re
import datetime
from reiwa.secondary import search_query
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class ReiwaDefault(object):
    reload(sys)
    sys.setdefaultencoding('utf8')
    def __init__(self, idb, item, spider):
        query = idb.dbpool.runInteraction(
            self.conditional_insert, item)
        # query.addErrback(idb.handle_error)
    def _preprocessing(self, item):
        if item is None or item['link'] == '':
            return None
        item['player_name'] = item['player_name'].replace('"', "'").\
        replace('^', '').\
        replace('&#8220;', "'").\
        replace('&#8221;', "'").\
        replace('&#8220', "'").\
        replace('&#8221', "'").\
        replace('&#8211', '-').\
        replace(';', ',').\
        replace('}', ']').\
        replace('{', '[').\
        replace(u'–', '-')
        try:
            if item['del_field'] is None:
                item['del_field'] = '0'
        except KeyError:
            item['del_field'] = '0'
        try:
            if item['create_tmp'] is None:
                item['create_tmp'] = str(datetime.datetime.now()).split('+')[0]
        except KeyError:
            item['create_tmp'] = str(datetime.datetime.now()).split('+')[0]
        return item
    def conditional_insert(self, tx, item):
        pass
