# write start_urls to redis
import redis

if __name__ == '__main__':
    REDIS_SERVER_IP = ''
    REDIS_PORT = ''
    REDIS_PASSWD = ''
    redisDb = redis.Redis(host=REDIS_SERVER_IP, port=REDIS_PORT, db=0, password=REDIS_PASSWD)

    redisUrlName = ''
    urls = []
    try:
        for url in urls:
            redisDb.rpush(redisUrlName, url)
    except Exception as e:
        print(e)