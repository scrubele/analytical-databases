from app import app
from urllib.request import urlopen
import json
from app.loggers import context
from app.redis_py import r

MAX_ROW_NUMBER = 200
OFFSET = 100


class DataProcessor:

    def __init__(self, url, limit):
        self.base_url = url
        self.limit = limit

    def get_data_from_url(self, offset):
        url = f'{self.base_url}?$limit={self.limit}&$offset={offset}'
        response = urlopen(url)
        data = json.load(response)
        context.do_logging(f"rows {offset}-{offset+self.limit} added")
        r.set(
            f"file {self.base_url} rows {offset}-{offset+self.limit}", "Completed")
        print(r.get(f"file {self.base_url} rows {offset}-{offset+self.limit}"))
        return data

    def loop_data(self):
        try:
            does_file_exists = r.get(f"file {self.base_url}")
            print(does_file_exists)
            if does_file_exists == b"Completed":
                r.set(f"file {self.base_url}", "Retry attempt, ignore a file")
                print(r.get(f"file {self.base_url}"))
                return "Retry attempt, ignore a file"
        except Exception:
            context.do_logging("Started loading data from: " + self.base_url)
            r.set(f"file {self.base_url}", "Started")
            print(r.get(f"file {self.base_url}"))
            offset = 0
            all_data = []
            while (offset < MAX_ROW_NUMBER):
                data = self.get_data_from_url(offset)
                offset += OFFSET
                all_data += data

            r.set(f"file {self.base_url}", "Completed")
            return all_data
