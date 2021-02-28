# -*- coding: utf-8 -*-
import scrapy


class XcfoneSpider(scrapy.Spider):
    name = 'xcfone'
    allowed_domains = ['xiachufang.com']
    start_urls = ['http://xiachufang.com/']

    def parse(self, response):
        pass
