# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        re_selector=response.xpath('//*[@id="post-110287"]/div[1]/h1')
        print re_selector
        re2_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
        re3_selector = response.xpath('//div[@class="entry-header"]/h1/text()')
        print re2_selector
        print re3_selector
        title=response.xpath()
        create_date=response.xpath()
        praise_nums=response.xpath()
        fav_nums=response.xpath()
        match_re=re.match(".*?(\d+).*",fav_nums)
        if match_re:
            fav_nums=match_re.groups(1)

        comment_nums=response.xpath()
        match_re=re.match(".*?(\d+).*",comment_nums)
        content=response.xpath("//div[@class='entry'])").extract()[0]


