# read items from redis
import redis
import time


if __name__ == '__main__':
    REDIS_SERVER_IP = ''
    REDIS_PORT = ''
    REDIS_PASSWD = ''
    redisDb = redis.Redis(host=REDIS_SERVER_IP, port=REDIS_PORT, db=0, password=REDIS_PASSWD)

    redisUrlName = ''
    while True:
        try:
            if redisDb.llen(redisUrlName) > 0:
                redisDb.blpop(redisUrlName, 100)[1]
            else:
                time.sleep(1)
        except Exception as e:
            print(e)