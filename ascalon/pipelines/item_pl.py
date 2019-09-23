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
            print item

            # query = (
            #     'INSERT IGNORE INTO item_weapon (item_cate, item_class, name, name_ko, '
            #     'req_level, req_str, req_dex, req_int, req_luk, str, dex, int, luk, hp, mp, '
            #     'watk, matk, wdef, mdef, acc, avoid, durability, upgrade_slot, available, '
            #     'atk_speed, speed, jump, ignore_def, boss_dmg, starforce, image_link) '
            #     'VALUES'
            #     '(%d, "%s", "%s", "%s", %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, '
            #     '%d, %d, %d, %d, %d, %d, %d, %d, "%s", %d, %d, %d, "%s", "%s", %d, "%s"'
            #     % (int(item['item_cate']), unicode(item['item_class']), unicode(item['name']),
            #         unicode(item['name_ko']), int(item['req_level']), int(item['req_str']), 
            #         int(item['req_dex']), int(item['req_int']), int(item['req_luk']),
            #         int(item['str']), int(item['dex']), int(item['int']), int(item['luk']),
            #         int(item['hp']), int(item['mp']), int(item['watk']), int(item['matk']),
            #         int(item['wdef']), int(item['mdef']), int(item['acc']), int(item['avoid']),
            #         int(item['durability']), int(item['upgrade_slot']), unicode(item['available']),
            #         int(item['atk_speed']), int(item['speed']), int(item['jump']),
            #         unicode(item['ignore_def']), unicode(item[''])
            #     )
            # )

            # query = (
            #     'INSERT IGNORE INTO job (job_name, `class`, main_stat, '
            #     'main_atk, affiliation, create_tmp) '
            #     'VALUES'
            #     '("%s", "%s", "%s", "%s", "%s", "%s")'
            #     % (unicode(item['job_name']), unicode(item['job_class']), unicode(item['main_stat']),
            #         unicode(item['main_atk']), unicode(item['affiliation']), unicode(item['create_tmp'])
            #     )
            # )

            # print query
            # tx.execute(query)

        except Exception as e:
            print e