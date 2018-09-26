# -*- coding: utf-8 -*-
import scrapy
from meizi.items import FangjiaItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://lianjia.com/']

    def parse(self, response):
        pass

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://hz.fang.lianjia.com/loupan/rs/']

    def parse(self, response):
        item=FangjiaItem()
        blocks=response.xpath('//div[@class="resblock-desc-wrapper"]')
        for block in blocks:
            name=block.xpath('//div [@class="resblock-name"]/a/text()').extract()
            print 'name'
            print name

            item['name']=name
            locations=block.xpath('//div[@class="resblock-location"]/span/text()')



