# -*- coding: utf-8 -*-
# import MySQLdb
import pymysql
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

def search_query(q, write=False):
    try:
        setting = settings.get('READ_DB_CONNECT')
        db = pymysql.conn(host = setting['host'],
                             user = setting['user'],
                             passwd = setting['passwd'],
                             db = setting['db'],
                             use_unicode = setting['use_unicode'],
                             charset = setting['charset'])
        cursor = db.cursor()
        cursor.execute(q)
        if write is True:
            db.commit()
            data = None
        else:
            data = cursor.fetchall()
        return data

    except Exception as e:
        print e
        return None

    finally:
        cursor.close()
        db.close()
