import json

import crochet
from flask import Flask
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scraper.spiders.behance import BehanceSpider

crochet.setup()
crawl_runner = CrawlerRunner()
app = Flask(__name__)

data = {}


@crochet.wait_for(timeout=60.0)
def scrape(username):
    data[username] = []

    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    return crawl_runner.crawl(BehanceSpider, username=username)


def _crawler_result(item, response, spider):
    data[spider.username].append(dict(item))


@app.route('/profile/<username>')
def profile(username):
    scrape(username)

    return json.dumps(data.get(username))
