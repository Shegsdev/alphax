# -*- coding: utf-8 -*-
from .spider import Crawler


class JobbermanSpider(Crawler):
    name = 'jobberman'
    allowed_domains = ['jobberman.com']
    static_url = 'http://jobberman.com/'

    def __init__(self, **kwargs):
        super(JobbermanSpider, self).__init__(**kwargs)
