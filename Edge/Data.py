from Handler import Handler
import time
from datetime import datetime

class Data:
    handler = Handler()

    def __init__(self, name, value, realTimeDatabase, timestamp=None, tag=None):
        self.name = name
        self.value = value
        self.realTimeDatabase = realTimeDatabase
        self.tag = tag
        self.timestamp = timestamp or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    def prepareData(self):
        if (self.realTimeDatabase):
            self.handler.sendRealTimeData(self.toRealtimeJson())

    def toRealtimeJson(self):
        if isinstance(self.timestamp, datetime):
            ts = self.timestamp.replace(tzinfo=None).isoformat() + "Z"
        else:
            ts = self.timestamp

        data = {
            "name": self.name,
            "value": self.value,
            "timestamp": ts
        }

        if self.tag is not None:
            data["tag"] = self.tag
        return data
