# The integration between Azure Redis Cache and Azure Event Hubs


**Installation via `requirements.txt`**:

```shell
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 runserver.py
```


**Add .env сonfig file with the next content:**
```
CONSOLE_LOGGING = False
WRITE_TO_REDIS = False

#Redis
REDIS_HOST_NAME = "example.redis.cache.windows.net"
REDIS_KEY = "enL88Gh80HBde7Od2kNj3HWYWBPlE0mnRt0KNGxgrmw="
#Event hub
EVENT_HUB_CONNNECTION_STRING = "Endpoint=sb://example.servicebus.windows.net/;SharedAccessKeyName=example;SharedAccessKey=muNgQGaRljw8llADlN4IWJY2dFYxLP8bLDkjHFQI4/I="
EVENT_HUB_NAME = "example"
CONSUMER_GROUP = "$Default"
#Storage
STORAGE_CONNNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=example;AccountKey=xKIJUalbEpzis97zd7U0IX+mxL7S3Ly+6xakK9kyKIoprZ66H5GMZ0VDJ34+zaNXwx7DNYtCvPXuBR0BH2R9wQ==;EndpointSuffix=core.windows.net"
BLOB_NAME = "example"
``

If CONSOLE_LOGGING is True -> logs are going to console, False -> logs are going to Azure Event Hub.