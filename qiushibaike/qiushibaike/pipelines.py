# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class QiushibaikePipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = self.connection.scrapy
        self.collection = self.db.qiushibaike

    def process_item(self, item, spider):
        if not self.connection or not item:
            return
        self.collection.save(item)

    def __del__(self):
        if self.connection:
            self.connection.close()
