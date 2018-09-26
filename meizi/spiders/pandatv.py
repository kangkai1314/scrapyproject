# -*- coding: utf-8 -*-
import scrapy


class PandatvSpider(scrapy.Spider):
    name = 'pandatv'
    allowed_domains = ['pandatv.com']
    start_url=['http://www.huaban.com']

    def parse(self, response):
        title=response.css('title::text').extract_first()
        title1=response.xpath('//head/title/text()').extract()
        print 'title'
        print title1
        print title
