import os


class Config(object):
    #Redus
    REDIS_HOST_NAME = "redis-iot-lab1.redis.cache.windows.net"
    REDIS_KEY = "enL88Gh80HBde7Od2kNj3HWYWBPlE0mnRt0KNGxgrmw="
    #Event hub
    EVENT_HUB_CONNNECTION_STRING = "Endpoint=sb://redis-iot-lab.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1ydxELyPYbfZnb/FfBjg9NiYTZu7I2Y/m9CB4dQOrvs="
    EVENT_HUB_NAME = "redis-iot-lab"
    CONSUMER_GROUP = "$Default"
    #Storage
    STORAGE_CONNNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=redisiotlab;AccountKey=xKIJUalbEpzis97zd7U0IX+mxL7S3Ly+6xakK9kyKIoprZ66H5GMZ0VDJ34+zaNXwx7DNYtCvPXuBR0BH2R9wQ==;EndpointSuffix=core.windows.net"
    BLOB_NAME = "redis"
    
    SECRET_KEY = os.urandom(32)
    APP_FOLDER = 'app/'
    TEMP_FOLDER = ".temp/"
    UPLOAD_FOLDER = APP_FOLDER + TEMP_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        os.mknod(UPLOAD_FOLDER+"__init__.py")
    # HEADERS
    CORS_HEADERS = 'Content-Type'
