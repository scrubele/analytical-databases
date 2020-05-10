import redis

myHostname = "redis-iot-lab1.redis.cache.windows.net"
myPassword = "enL88Gh80HBde7Od2kNj3HWYWBPlE0mnRt0KNGxgrmw="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

result = r.set("Message", "Hello!, The cache is working with Python!")
print("SET Message returned : " + str(result))

result = r.get("Message")
print("GET Message returned : " + result.decode("utf-8"))

result = r.client_list()
print("CLIENT LIST returned : ")
for c in result:
    print("id : " + c['id'] + ", addr : " + c['addr'])

from urllib.request import urlopen
import json
print('here')
response = urlopen(f'https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit={100}&$offset={100}')
data = json.load(response)   
print (data)