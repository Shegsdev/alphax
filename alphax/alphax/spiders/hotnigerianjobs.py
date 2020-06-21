# -*- coding: utf-8 -*-

from .spider import Crawler


class HotNigerianJobSpider(Crawler):
    name = 'hotnigerianjobs'
    allowed_domains = ['hotnigerianjobs.com']
    static_url = 'http://www.hotnigerianjobs.com/state/lagos/0/jobs-in-lagos-state/'

    def __init__(self, **kwargs):
        super(HotNigerianJobSpider, self).__init__(**kwargs)
