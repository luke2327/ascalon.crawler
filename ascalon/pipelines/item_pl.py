# -*- coding: utf-8 -*-

import sys
import re
import logging
import datetime
from ascalon.pipelines.default import AscalonDefault

class ItemPL(AscalonDefault):
    reload(sys)
    sys.setdefaultencoding('utf8')
    def __init__(self, idb, item, spider):
        super(ItemPL, self).__init__(idb, item, spider)
    def conditional_insert(self, tx, item):
        if item is None:
            return None
        ### 1. Insert Vod
        # Make Insert Vod Query

        item = self._preprocessing(item)
        try:
            sql = 'INSERT IGNORE INTO item_weapon ('
            for data in item.items():
                if data[1] is not None:
                    sql += data[0] + ', '

            sql = sql[:-2] + ') VALUES ('

            for data in item.items():
                if data[1] is not None:
                    if type(data[1]) is unicode or type(data[1]) is str:
                        sql += '"' + unicode(data[1]) + '", '
                    else:
                        sql += unicode(data[1]) + ', '

            sql = sql[:-2] + ')'

            tx.execute(sql)
        except Exception as e:
            print e