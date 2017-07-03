# -*- coding: utf-8 -*-

# Scrapy settings for Distrubute_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Distrubute_scrapy'

SPIDER_MODULES = ['Distrubute_scrapy.spiders']
NEWSPIDER_MODULE = 'Distrubute_scrapy.spiders'


LOG_LEVEL = 'INFO'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

COOKIES_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
}

ITEM_PIPELINES = {
}

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

REDIS_START_URLS_BATCH_SIZE = 1

# Schedule requests using a queue (FIFO).
SCHEDULER_QUEUE_CLASS = 'distrubute_scrapy.scrapy_redis.queue.SpiderPriorityQueue'