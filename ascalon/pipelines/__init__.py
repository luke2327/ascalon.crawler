import logging
import sys
from ascalon.pipelines.rating_pl import RatingPL
from ascalon.pipelines.notice_pl import NoticePL
from ascalon.pipelines.item_pl import ItemPL
from ascalon.pipelines.vod_pl import VodPL
from ascalon.pipelines.job_pl import JobPL
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
        elif spider.__class__.__name__[0:6] == 'Notice':
            pipeline_class = globals()['NoticePL']
        elif spider.__class__.__name__[0:4] == 'Item':
            pipeline_class = globals()['ItemPL']
        elif spider.__class__.__name__[0:3] == 'Vod':
            pipeline_class = globals()['VodPL']
        elif spider.__class__.__name__[0:3] == 'Job':
            pipeline_class = globals()['JobPL']
        else:
            pipeline_class = globals()[spider.__class__.__name__+"PL"]

        pipeline_class(self, item, spider)

        return item
