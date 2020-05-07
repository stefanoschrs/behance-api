# -*- coding: utf-8 -*-
import scrapy
from json import loads as json_loads


class BehanceSpider(scrapy.Spider):
    name = 'behance'
    allowed_domains = ['behance.net']

    def __init__(self, username='', **kwargs):
        if username == '':
            raise ValueError('missing username')

        self.username = username
        self.start_urls = ['https://behance.net/' + self.username]
        super().__init__(**kwargs)

    def parse(self, response):
        data = json_loads(response.css('#beconfig-store_state::text').get())

        for project in data['profile']['activeSection']['work']['projects']:
            yield scrapy.Request(
                project['url'],
                callback=self.parse_project)

    @staticmethod
    def parse_project(response):
        data = json_loads(response.css('#beconfig-store_state::text').get())

        yield data['project']['project']
