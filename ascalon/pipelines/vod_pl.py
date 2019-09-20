# -*- coding: utf-8 -*-

import sys
import re
import logging
import datetime
from ascalon.pipelines.default import AscalonDefault

class VodPL(AscalonDefault):
    reload(sys)
    sys.setdefaultencoding('utf8')
    def __init__(self, idb, item, spider):
        super(VodPL, self).__init__(idb, item, spider)
    def conditional_insert(self, tx, item):
        if item is None:
            return None
        ### 1. Insert Vod
        # Make Insert Vod Query

        item = self._preprocessing(item)
        try:
            query = (
                'INSERT IGNORE INTO vod (title, game, '
                '`source`, link, image_link, `duration`, create_tmp, before_tmp, auth) '
                'VALUES'
                '("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
                % (unicode(item['title']), item['game'], item['source'],
                    unicode(item['link']), unicode(item['image_link']),
                    unicode(item['duration']), unicode(item['create_tmp']), 
                    item['before_tmp'], item['auth']
                )
            )

            print query
            tx.execute(query)
        except Exception as e:
            print 'hello'
            print e
        # rating_id = tx.lastrowid
