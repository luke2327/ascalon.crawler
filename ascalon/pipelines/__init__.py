import logging
import sys
from ascalon.pipelines.rating_pl import RatingPL
from ascalon.pipelines.vod_pl import VodPL
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class InsertDB(object):
    def __init__(self):
        dbargs = settings.get('DB_CONNECT')
        db_server = settings.get('DB_SERVER')
        dbpool = adbapi.ConnectionPool(db_server, **dbargs)
        self.dbpool = dbpool
    def process_item(self, item, spider):
        if spider.__class__.__name__[0:6] == 'Rating':
            pipeline_class = globals()['RatingPL']
        elif spider.__class__.__name__[0:3] == 'Vod':
            pipeline_class = globals()['VodPL']
        else:
            pipeline_class = globals()[spider.__class__.__name__+"PL"]
        pipeline_class(self, item, spider)
        return item
