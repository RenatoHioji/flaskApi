from redis import Redis

connection = Redis(host="redis")

def testdb():
    connection.set('my_key', 'Hello, Redis!')
    value_from_redis = connection.get('my_key')
    return f"Hello world! Value from Redis:{value_from_redis}"