# -*- coding: utf-8 -*-
import scrapy

from firstproject.items import FirstprojectItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/basketball/nba/2019-05-09/doc-ihvhiqax7645328.shtml',
                  'http://sports.sina.com.cn/basketball/nba/2019-05-09/doc-ihvhiews0833865.shtml',
                  'http://sports.sina.com.cn/basketball/nba/2019-05-09/doc-ihvhiews0793383.shtml']

    def parse(self, response):
        item = FirstprojectItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(item["urlname"])
