import dramatiq
import requests
from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="redis.base.svc.cluster.local", port=6379)
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def count_words(url):
    print(url)

count_words.send("http://example.com")