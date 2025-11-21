from MqttPublisher import MqttPublisher
import json
from dotenv import load_dotenv
import os

load_dotenv()

TOPIC_PREFIX = os.getenv("TOPIC_PREFIX")
TOPIC_SUFFIX_REALTIME = os.getenv("TOPIC_SUFFIX_REALTIME")
TOPIC_SUFFIX_SQL = os.getenv("TOPIC_SUFFIX_SQL")

if not all([TOPIC_PREFIX, TOPIC_SUFFIX_REALTIME, TOPIC_SUFFIX_SQL]):
    raise ValueError("TOPIC_PREFIX, TOPIC_SUFFIX_REALTIME eller TOPIC_SUFFIX_SQL mangler i .env")

class Handler:
    _instance = None
    mqtt = MqttPublisher()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sendRealTimeData(self, data_json):
        self.mqtt.publish(json.dumps(data_json), TOPIC_PREFIX, TOPIC_SUFFIX_REALTIME)

    def sendSQLData(self, data_json):
        self.mqtt.publish(json.dumps(data_json), TOPIC_PREFIX, TOPIC_SUFFIX_SQL)
