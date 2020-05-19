from environs import Env

env = Env()
env.read_env()

CONSOLE_LOGGING = env.bool("CONSOLE_LOGGING")
WRITE_TO_REDIS = env.bool("WRITE_TO_REDIS")


class Config:
    #Redus
    REDIS_HOST_NAME = env.str("REDIS_HOST_NAME")
    REDIS_KEY = env.str("REDIS_KEY")
    #Event hub
    EVENT_HUB_CONNNECTION_STRING = env.str("EVENT_HUB_CONNNECTION_STRING")
    EVENT_HUB_NAME = env.str("EVENT_HUB_NAME")
    CONSUMER_GROUP = env.str("CONSUMER_GROUP")
    #Storage
    STORAGE_CONNNECTION_STRING = env.str("STORAGE_CONNNECTION_STRING")
    BLOB_NAME = env.str("BLOB_NAME")