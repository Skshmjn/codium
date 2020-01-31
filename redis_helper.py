import redis

r = redis.Redis(host='localhost', port=6379, db=0)
# seq = [1, 2, 3]

r.rpush('key', 5)
print(r.lrange('key', 0, -1))
print(r.lrem('key', 0, r.lindex('key', 1)))
print(r.lrange('key', 0, -1))
