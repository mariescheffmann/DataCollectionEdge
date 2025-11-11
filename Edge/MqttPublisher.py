import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

class MqttPublisher:
    def __init__(self):
        load_dotenv()
        self.client = mqtt.Client(client_id=os.getenv("CLIENT_ID"), protocol=mqtt.MQTTv311)
        self.client.connect(os.getenv("BROKER"), int(os.getenv("PORT")), 60)

    def publish(self, message, topic):
        self.client.publish(topic, message)
