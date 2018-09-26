# -*- coding: utf-8 -*-
import scrapy


class MeiziaSpider(scrapy.Spider):
    name = 'meizia'
    allowed_domains = ['mm131.com']
    start_urls = ['http://www.mm131.com/xinggan/']

    def parse(self, response):
        list = response.css(".list-left dd:not(.page)")
        title=response.css('title::text').extract_first()
        for img in list:
            name=img.css('a::text').extract_first().encode('utf-8')
            url=img.css('a::attr(href)').extract_first()

            print url
            url2=str(url)
            #print url2
            yield scrapy.Request(url2,callback=self.content)

    def content(self,response):
        from meizi.items import MeiziItem
        item=MeiziItem()
        item['name']=response.css(".content h5::text").extract_first()
        #print item['name']
        item['url']=response.css(".content-pic img::attr(src)").extract_first()
        yield item







