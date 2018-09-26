# -*- coding: utf-8 -*-
import scrapy
from meizi.items import JobfinderItem

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?industries=&dqs=070020&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=15&flushckid=1&fromSearchBtn=2&headckid=16a4c5b6c89e89fa&d_headId=4b8143ff4fd53032d13380e22c855c04&d_ckId=4b8143ff4fd53032d13380e22c855c04&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&key=python']

    def parse(self, response):
        item=JobfinderItem()
        joblist=response.xpath('//div[@class="sojob-item-main clearfix"]')
        for job in joblist:
            name=job.xpath('//a/text()').extract()

