from environs import Env

env = Env()
env.read_env()

CONSOLE_LOGGING = env.bool("CONSOLE_LOGGING")
WRITE_TO_REDIS = env.bool("WRITE_TO_REDIS")