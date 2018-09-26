# -*- coding: utf-8 -*-
import scrapy
from meizi.items import PandatvItem


class HuabanSpider(scrapy.Spider):
    name = 'huaban'
    allowed_domains = ['huaban.com']
    start_urls = ['http://pandatv.com/all']


    def parse(self, response):

        title=response.css('title::text').extract_first()
        title1=response.xpath('//head/title/text()').extract_first()
        print title
        print title1
        videos=response.css('.video-list ')

        videos1=response.xpath('//*[@id="later-play-list"]/li')
        #videos1_list=videos1.xpath('//li[@class="video-list-item"]')
        videos_list=response.css('li.video-list-item.video-no-tag')
        #print videos_list
        for video in videos_list:
            nickname=video.css('span.video-nickname::attr(title)').extract_first()
            number=video.css('span.video-number::text').extract_first()
            real_num=video.css('i.video-station-num::text').extract_first()

            item = PandatvItem(name=nickname,people_num=number,station_num=real_num)
            yield item














