# -*- coding: utf-8 -*-

import sys
import imp
import re
import logging
import datetime
from ascalon.pipelines.default import AscalonDefault

class NoticePL(AscalonDefault):
    imp.reload(sys)
    # sys.setdefaultencoding('utf8')

    def __init__(self, idb, item, spider):
        super(NoticePL, self).__init__(idb, item, spider)

    def conditional_insert(self, tx, item):
        if item is None:
            return None
        ### 1. Insert Notice
        # Make Insert Notice Query

        item = self._preprocessing(item)
        try:
            query = (
                'INSERT IGNORE INTO notice (type, title, '
                'published_date, `desc`, region, link) '
                'VALUES'
                '(%s, %s, %s, %s, %s, %s) '
            )

            tx.execute(query, (item['type'], item['title'], item['published_date'],
                    item['desc'], item['region'], item['link']))
        except Exception as e:
            print(e)
