# Distributed_scrapy
基于scrapy-redis写的一个简单的分布式爬虫

需要安装scrapy 和 redis数据库

**如何运行**

- 首先运行redis

- 然后启动一个进程，向redis中写入初始url， 其key需保持与spider中的redis_key一致

- 运行scrapy爬虫程序。可同时开启多个爬虫。pipeline中的item保存在redis数据库中，默认key值见scrapy_redis/pipelines.py

- 启动一个进程，从redis中的保存item的队列中获取数据，并持久化至相应数据库。
