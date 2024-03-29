# -*- coding: utf-8 -*-

import sys
import imp
import re
import logging
import datetime
from ascalon.pipelines.default import AscalonDefault

class RatingPL(AscalonDefault):
    imp.reload(sys)
    # sys.setdefaultencoding('utf8')

    def __init__(self, idb, item, spider):
        super(RatingPL, self).__init__(idb, item, spider)

    def conditional_insert(self, tx, item):
        if item is None:
            return None
        ### 1. Insert Rating
        # Make Insert Rating Query

        item = self._preprocessing(item)
        try:
            query = (
                'INSERT IGNORE INTO UserInfo (player_name, game, '
                '`source`, `rank`, link, create_tmp) '
                'VALUES'
                '("%s", "%s", "%s", %s, "%s", '
                'DATE_ADD(now(), INTERVAL RAND()*60 SECOND)) '
                % (unicode(item['player_name']), item['game'], item['source'],
                str(item['rank']), unicode(item['link']))
            )

            tx.execute(query)

        except Exception as e:
            print(e)
        # rating_id = tx.lastrowid
