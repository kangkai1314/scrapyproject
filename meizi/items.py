# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiziItem(scrapy.Item):
    name=scrapy.Field()
    url=scrapy.Field()

class JobfinderItem(scrapy.Item):
    job_name=scrapy.Field()
    job_salary=scrapy.Field()
    job_location=scrapy.Field()
    job_enducation=scrapy.Field()
    job_experience=scrapy.Field()
    job_company=scrapy.Field()
    job_url=scrapy.Field()
    job_desc=scrapy.Field()

class FangjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    addr=scrapy.Field()
    price=scrapy.Field()
    imageurl=scrapy.Field()

class HuabanItem(scrapy.Item):
    name=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()

class PandatvItem(scrapy.Item):
    name=scrapy.Field()
    people_num=scrapy.Field()
    station_num=scrapy.Field()


