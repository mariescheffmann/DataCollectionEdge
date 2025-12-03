import paho.mqtt.client as mqtt
import os
import ssl
from dotenv import load_dotenv

class MqttPublisher:
    def __init__(self):
        load_dotenv()
        self.client = mqtt.Client(client_id=os.getenv("CLIENT_ID"))
        self.client.tls_set(
            ca_certs="certs/ca.crt",
            certfile="certs/edge-client.crt",
            keyfile="certs/edge-client.key",
            tls_version=ssl.PROTOCOL_TLSv1_2
        )
        self.client.tls_insecure_set(True)

        self.client.connect(os.getenv("BROKER"), int(os.getenv("PORT")), 60)

    def publish(self, message, topic_prefix, topic_suffix):
        client_id = os.getenv("CLIENT_ID")
        topic = f"{topic_prefix}/{client_id}/{topic_suffix}"
        self.client.publish(topic, message)
