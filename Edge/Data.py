from Handler import Handler
import time
from datetime import datetime

handler = Handler()

class Data:
    def __init__(self, name, value, realTimeDatabase, timestamp=None, tag=None):
        self.name = name
        self.value = value
        self.realTimeDatabase = realTimeDatabase
        self.tag = tag
        self.timestamp = timestamp or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    def prepareData(self):
        if (self.realTimeDatabase):
            handler.sendRealTimeData(self.toRealtimeJson())

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

class EventPayload:
    def __init__(self, machine_id, event_name, opcua_value, template_config, timestamp=None):
        self.machine_id = machine_id
        self.event_name = event_name
        self.opcua_value = opcua_value
        self.template_config = template_config
        self.timestamp = timestamp or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    def toSQLJson(self):
        if isinstance(self.timestamp, datetime):
            ts = self.timestamp.replace(tzinfo=None).isoformat() + "Z"
        else:
            ts = self.timestamp

        payload = {
            "machine_id": self.machine_id,
            "event_name": self.event_name,
            "opcua_value": self.opcua_value,
            "template_config": self.template_config,
            "timestamp": ts
        }

        return payload

    def sendData(self):
        handler.sendSQLData(self.toSQLJson())
