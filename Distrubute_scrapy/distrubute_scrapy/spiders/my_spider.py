# -*- coding: utf-8 -*-

# 爬取新浪用户的所有微博，顺便记录下用户信息
from distrubute_scrapy.items import DistrubuteScrapyItem
from distrubute_scrapy.scrapy_redis.spiders import RedisSpider
import logging


class MySpider(RedisSpider):
    name = 'my_spider'  # 爬虫名称
    allowed_domain = ['']  # 访问的url的域名
    redis_key = 'my_redis_key:start_urls'

    def __init__(self, *args, **kwargs):
        logging.info('-----initiating WblogSpider------')
        super(MySpider, self).__init__(*args, **kwargs)

    # 解析页面
    def parse(self, response):
        logging.info("parse : " + response.url)
        item = DistrubuteScrapyItem()
        return item

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
