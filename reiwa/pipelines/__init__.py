import logging
import sys
from reiwa.pipelines.rating_pl import RatingPL
from reiwa.secondary import search_query
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class InsertDB(object):
    def __init__(self):
        dbargs = settings.get('DB_CONNECT')
        db_server = settings.get('DB_SERVER')
        # dbpool = adbapi.ConnectionPool(db_server, **dbargs)
        # self.dbpool = dbpool
        print 'hello'
    def process_item(self, item, spider):
        print 'nice'
        return item
