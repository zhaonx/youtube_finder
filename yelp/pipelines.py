# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymongo


class YelpPipeline:
    def __init__(self, settings):
        self.settings = settings
        self.handler = pymongo.MongoClient(self.settings['MONGODB_URI']).youtube.final_user

    @classmethod
    def from_crawler(cls, crawler):
        return cls(settings=crawler.settings)

    def process_item(self, item, spider):
        # info = dict(item)
        info_ = item['abc']
        info = {'url': info_['url'], 'name': info_['name'], 'keyword': info_['keyword'], 'ts': info_['ts'],
                'has_keyword_in_bio': info_['has_keyword_in_bio'], 'language': info_['language'],
                'has_location_keyword_time_in_videos': info_['has_location_keyword_time_in_videos']}
        self.handler.insert_one(info)
        return item
