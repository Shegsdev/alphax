# -*- coding: utf-8 -*-
import scrapy


class JobbermanSpider(scrapy.Spider):
    name = 'jobberman'
    allowed_domains = ['jobberman.com']
    start_urls = ['http://jobberman.com/']

    def parse(self, response):
        pass
