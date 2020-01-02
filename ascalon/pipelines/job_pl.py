# -*- coding: utf-8 -*-

import sys
import re
import logging
import datetime
from ascalon.pipelines.default import AscalonDefault

class JobPL(AscalonDefault):
    reload(sys)
    sys.setdefaultencoding('utf8')

    def __init__(self, idb, item, spider):
        super(JobPL, self).__init__(idb, item, spider)

    def conditional_insert(self, tx, item):
        if item is None:
            return None
        ### 1. Insert Job
        # Make Insert Job Query

        item = self._preprocessing(item)
        try:
            query = (
                'INSERT IGNORE INTO job (job_name, `class`, main_stat, '
                'main_atk, affiliation, create_tmp) '
                'VALUES'
                '("%s", "%s", "%s", "%s", "%s", "%s")'
                % (unicode(item['job_name']), unicode(item['job_class']), unicode(item['main_stat']),
                    unicode(item['main_atk']), unicode(item['affiliation']), unicode(item['create_tmp'])
                )
            )

            tx.execute(query)

        except Exception as e:
            print 'hello'
            print e
        rating_id = tx.lastrowid
