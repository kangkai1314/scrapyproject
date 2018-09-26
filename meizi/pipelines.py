# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import re
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline
class MeiziPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    def __init__(self):
        self.host='127.0.0.1'
        self.port=27017
        client=pymongo.MongoClient(self.host,self.port)
        db=client['ScrapyChina']
        self.post=db['mingyan']

    def process_item(self,item,spider):
        postItem=dict(item)
        self.post.insert(postItem)
        return item


class MeiziImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):

        for i in item:
            #print url
            #print item['name']
            yield Request(url,meta={'item':item['name']})


    def file_path(self, request, response=None, info=None):

        name=request.meta['item']
        name=re.sub(r'[?\\*|"<>:/()0123456789]','',name)
        image_guid=request.url.split('/')[-1]
        filename=u'full/{0}/{1}'.format(name,image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path=[x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths']=image_path
        return item






