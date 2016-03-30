# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    skill_set = scrapy.Field()
    url = scrapy.Field()
    pass
