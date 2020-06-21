import os
import json
import scrapy

from datetime import datetime
from .thread import worker
from .utils import read_content, append_to_file, create_directory_file, get_domain_name

from urllib.parse import urlparse


class Crawler(scrapy.Spider):
    name = ""
    static_url = ""
    search_result_urls = ""

    def __init__(self, **kwargs):
        super(Crawler, self).__init__(**kwargs)

        if not self.static_url:
            raise Exception('no urls to crawl')

    def start_requests(self):
        yield scrapy.Request(self.static_url, self.parse)

    def parse(self, response):
        urls = response.css('span.jobheader a::attr(href)').getall()

        parsed_uri = urlparse(self.static_url)
        domain_name = '{uri.netloc}'.format(uri=parsed_uri)
        domain = get_domain_name(domain_name)

        for href in urls:
            path = 'visited/' + domain + '/' + '/visited.txt'
            create_directory_file('visited/' + domain, path)

            if href not in open(path).read():
                data = read_content(href)
                if data is not None:
                    worker(Crawler.save_json(domain, data))
                append_to_file(path, href)

        # next_pages = response.xpath(self.next_page).getall()
        # if next_pages is not None:
        #     for next_page in next_pages:
        #         yield response.follow(next_page, callback=self.parse, meta={'tenant': tenant})

    def closed(self, reason):
        parsed_uri = urlparse(self.static_url)
        print('closing...', parsed_uri)

    @staticmethod
    def save_json(source, data_list):
        date = datetime.now().strftime("%B %d %Y")
        path = f'crawled/jobs/{ source }/{ date }/crawled.json'
        basedir = os.path.dirname(path)

        create_directory_file(basedir, path)
        with open(path, 'r') as infile:
            try:
                file_in = infile.read()
                if not file_in:
                    file_in = '[]'
                results = json.loads(file_in, encoding="utf-8")
                results += data_list

                with open(path, 'w') as outfile:
                    json.dump(results, outfile, indent=2)
            except Exception as e:
                print(e)  # for the repr
                print(str(e))  # for just the message
                print(e.args)
                with open(path, 'w') as empty:
                    empty.write('[]')
